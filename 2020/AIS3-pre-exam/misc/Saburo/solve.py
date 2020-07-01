#!/usr/bin/env python3
import time
import string
from pwn import *
import threading

flag = 'AIS3{A1r1ght_U_4r3_my_3n3nnies}'

lock = threading.Lock()
scores = []

def oracle(m):
    context.log_level = 'ERROR'
    r = remote('60.250.197.227', 11001)
    r.sendlineafter('Flag: ', m)
    new_score = int(r.recvline().strip().split(b' ')[4])
    r.close()
    with lock:
        scores.append(new_score)

def average(m):
    global scores

    scores = []

    threads = []
    for i in range(20):
        threads.append(threading.Thread(target = oracle, args = (m,)))
        threads[-1].start()

    for i in range(20):
      threads[i].join()

    return sum(scores) / len(scores)

s = string.ascii_letters + string.digits + '{_-+}'

while True:
    new_scores = []
    for c in s:
        new_score = average(flag + c)
        print(f'{flag+c} : {new_score}')
        new_scores.append(float(new_score))
    idx = new_scores.index(max(new_scores))
    flag += s[idx]
    print(flag)
