import time
from z3 import *
from pwn import *
from itertools import *

def enc(x):
    return bytes([v ^ b"RICK"[i % 4] for i, v in enumerate(x.encode())])

gate_type = [None, Not, And, Or, Xor, And, Or]

class Gate:
    def __init__(self, challenge):
        self.challenge = challenge
        self.ptr = 0
        self.nodes = []

    def eat(self):
        self.ptr += 4
        return challenge[self.ptr-4:self.ptr]

    def parse(self):
        data = self.eat()
        node_type = u32(data) % 10

        # child node
        if node_type == 0:
            name = f'x_{len(self.nodes)}'
            self.nodes.append(Bool(name))
            return self.nodes[-1], name
        # not gate
        elif node_type == 1:
            self.eat()
            node, name = self.parse()
            return Not(node), f'1({name})'
        # normal gate
        elif 2 <= node_type <= 6:
            ans, names = None, []
            for i in range(self.eat()[0]):
                node, name = self.parse()
                names.append(name)
                if ans is None:
                    ans = node
                else:
                    ans = gate_type[node_type](ans, node)
            if 5 <= node_type <= 6:
                ans = Not(ans)
            return ans, f'{node_type}({", ".join(names)})'
        # 1010 or 0101 = True
        elif node_type == 7:
            nodes, names = [], []
            for i in range(self.eat()[0]):
                node, name = self.parse()
                nodes.append(node)
                names.append(name)
            _1 = nodes[0]
            for i, node in enumerate(nodes[1:]):
                if i % 2 == 0:
                    _1 = And(_1, Not(node))
                else:
                    _1 = And(_1, node)
            _2 = Not(nodes[0])
            for i, node in enumerate(nodes[1:]):
                if i % 2 == 0:
                    _2 = And(_2, node)
                else:
                    _2 = And(_2, Not(node))
            return Or(_1, _2), f'7({", ".join(names)})'
        # Nor gate ( only apply head tail )
        elif node_type == 8:
            nodes, names = [], []
            for i in range(self.eat()[0]):
                node, name = self.parse()
                nodes.append(node)
                names.append(name)
            return Not(Or(nodes[0], nodes[-1])), f'8({", ".join(names)})'
        # And gate ( only apply head tail )
        elif node_type == 9:
            nodes, names = [], []
            for i in range(self.eat()[0]):
                node, name = self.parse()
                nodes.append(node)
                names.append(name)
            return And(nodes[0], nodes[-1]), f'9({", ".join(names)})'

r = remote('rick.challenges.ooo', 4343)

r.recvn(4) # RICK

level = 0
while True:
    print()
    print('----------')
    print(f'level = {(level := level + 1)}')
    
    length = u32(r.recvn(4))
    print(f'[+] length: {length * 4}')

    if length == u32(b'RICK'):
        r.recvn(4)
        print(xor(r.recv(), b'RICK' * 100))
        break

    challenge = r.recvn(length * 4)
    print(f'recv: {challenge.hex()}')
    if challenge.startswith(b'KO'):
        break

    # parse
    gate = Gate(challenge)
    node, name = gate.parse()
    print(f'[+] parse result: {name}')

    # solve
    s = Solver()
    s.add(node == BoolVal(True))
    if not s.check():
        print('FUCKFUCKFUCK')
        raise ValueError
    m = s.model()
    
    # build ans string
    command = ''
    for node in gate.nodes:
        command += str(int(bool(m[node])))

    # send
    print(f'[+] send: {command}')
    r.sendline(enc(command))

    print('----------')
    print()

