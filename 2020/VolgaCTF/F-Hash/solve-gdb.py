import gdb

def register(name):
    return int(gdb.parse_and_eval(name))

def read(address, size):
    inf = gdb.inferiors()[0]
    return inf.read_memory(address, size).tobytes()

def write(address, buf):
    inf = gdb.inferiors()[0]
    inf.write_memory(address, buf)

memory = {}
state = []

class Start(gdb.Breakpoint):
    def __init__(self, location):
        super(Start, self).__init__(spec = location, type = gdb.BP_BREAKPOINT, internal = False, temporary = False)
    def stop(self):
        state.append((register('$rdi'), register('$rsi'), register('$rdx'), register('$rcx')))
        if memory.get(state[-1][1:]) is not None:
            gdb.execute('set $rsi = 1')
            
class End(gdb.Breakpoint):
    def __init__(self, location):
        super(End, self).__init__(spec = location, type = gdb.BP_BREAKPOINT, internal = False, temporary = False)
    def stop(self):
        global state
        buf, h = state[-1][0], state[-1][1:]
        if memory.get(h) is None:
            memory[h] = (read(buf, 8), read(buf + 8, 8), read(buf + 16, 8))
        else:
            write(buf, memory[h][0])
            write(buf + 8, memory[h][1])
            write(buf + 16, memory[h][2])
        state = state[:-1]

Start(f'*{0x0000555555554000 + 0x13b0}')
End(f'*{0x0000555555554000 + 0x1424}')
