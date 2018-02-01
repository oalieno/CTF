#!/usr/bin/env python3
from pwn import *
from Crypto.Util.number import inverse

''' find p
now = 1399264912720503420925780748954523663537735823893141357015180483429860932204867156984546651385344483486720647363860298289

while True:
    print("now:    ", now)
    r = remote("random2win.acebear.site", 33337)
    r.sendlineafter("Your choice: ", "1")
    r.sendlineafter("Message: ", '\x00')
    r.recvuntil("Ciphertext: ")
    result = int(r.recvline().strip())
    print("result: ", result)
    now = max(now, result)
    r.sendlineafter("Message: ", now.to_bytes(100, 'big'))
    r.recvuntil("Ciphertext: ")
    result2 = int(r.recvline().strip())
    print("result2:", result2)
    if result2 > result: now = max(now, result)
    elif result2 < result: now += result - result2
    else:
        print("p:", now)
        break
    r.close()
'''

p = 2129236650498506197214865121017813676962270980934541379925587741818174020229784960110052122450619093813474017151250421361 # prime

''' find h
a = 1978674184720744196590300361325405779725352663258110448759637853475271480775575593700483047574172813739244992730981365692 # (r1 * h + 0) % p
b = 814858589047597154083822743048657549391974074420868531835580671285717281927461098238786959838165672805481848130353523144  # (r2 * h + 0) % p

aa = []
bb = []

for i in range(1, 222222 + 1):
    aa.append(a * inverse(i, p) % p)
    bb.append(b * inverse(i, p) % p)

print(set(aa) & set(bb))
'''

h = 11305546770736405378819894875529407145124231011999396912086973074056791191623579252993880901245430834195596982773094

low  = 10 ** 10
high = 10 ** 12
most = h * high // p

r = remote("random2win.acebear.site", 33337)
r.sendlineafter("Your choice: ", "2")
r.recvuntil("Ciphertext: ")
result = int(r.recvline().strip())
for i in range(most):
    now = i * p + result
    rand, m = now // h, now % h
    if low <= rand <= high and low <= m <= high:
        r.sendline(str(m))
        break
r.interactive()
