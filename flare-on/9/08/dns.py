from dnslib.server import *
from dnslib.dns import RR
from mt import MT

class MyResolver:
    def __init__(self):
        self.main_domain = "abcdefghijklmnopqrstuvwxyz0123456789"
        self.the_domain = "amsjl6zci20dbt35guhw7n1fqvx4k8y9rpoe"
        self.previous = None
        self.previous_ip = None
        self.now = 0
        self.path = [2, 10, 8, 19, 11, 1, 15, 13, 22, 16, 5, 12, 21, 3, 18, 17, 20, 14, 9, 7, 4]

    def resolve(self, request, handler):
        reply = request.reply()
        if request.q.qtype == 1:
            parts = [part.decode() for part in request.q.qname.label]
            if parts[-2] == "flare-on" and parts[-1] == "com":
                reply.add_answer(*RR.fromZone(f"{'.'.join(parts)} 60 A {self.handle(parts)}"))
        return reply

    def decode(self, x, domain):
        if isinstance(x, int):
            _x = ""
            while x > 0:
                _x = self.main_domain[x % 36] + _x
                x //= 36
            x = _x
        y = 0
        for i in x:
            y = y * 36 + domain.index(i)
        return y

    def decode_2(self, x, domain, domain_2):
        return self.decode(
            self.decode(x, domain),
            domain_2
        )

    def shuffle(self, s):
        mt = MT()
        mt.seed(s)
        domain_in = list(self.main_domain)
        domain_out = ""
        for i in range(36):
            num = mt.randint(0, len(domain_in))
            domain_out += domain_in[num]
            domain_in.remove(domain_in[num])
        return domain_out

    def handle(self, parts):
        name = '.'.join(parts)
        if self.previous == name:
            return self.previous_ip
        self.previous = name
        self.previous_ip = self._handle(parts)
        return self.previous_ip

    def _handle(self, parts):
        target = parts[0]
        name = '.'.join(parts)

        counter = self.decode(target[-3:], self.the_domain)
        current_domain = self.shuffle(counter)

        if len(target) == 5:
            agent_id = self.decode_2(target[:-3], current_domain, self.the_domain)
            ip = "129.0.0.2"

            print(f'{name} -> {agent_id} -> {ip}')

            return ip

        elif len(target) == 9:
            cat      = self.decode_2(target[:1], current_domain, self.the_domain)
            agent_id = self.decode_2(target[1:3], current_domain, self.the_domain)
            offset   = self.decode_2(target[3:6], current_domain, self.the_domain)
            
            cmd = (str(self.path[self.now]) + "\x00\x00\x00")[:3]
            self.now += 1
            self.now %= len(self.path)
            ip = f"43.{ord(cmd[0])}.{ord(cmd[1])}.{ord(cmd[2])}"
            
            print(f'{name} -> {cat} {agent_id} {offset} -> {ip}')
            
            return ip

        else:
            cat      = self.decode_2(target[:1], current_domain, self.the_domain)
            agent_id = self.decode_2(target[1:3], current_domain, self.the_domain)
            offset   = self.decode_2(target[3:6], current_domain, self.the_domain)
            size     = self.decode_2(target[6:9], current_domain, self.the_domain)

            if cat == 3:
                cmd = (str(self.path[self.now]) + "\x00\x00\x00")[:3]
                self.now += 1
                self.now %= len(self.path)
                ip = f"43.{ord(cmd[0])}.{ord(cmd[1])}.{ord(cmd[2])}"
            else:
                ip = f"129.0.0.{len(str(self.path[self.now])) + 1}"

            print(f'{name} -> {cat} {agent_id} {offset} {size} -> {ip}')

            return ip

logger = DNSLogger(prefix=False, logf=lambda s: None)
server = DNSServer(MyResolver(), port=53, address="localhost", logger=logger)
server.start_thread()

while True:
    pass
