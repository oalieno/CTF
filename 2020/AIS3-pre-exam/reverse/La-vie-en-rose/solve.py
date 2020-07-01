#!/usr/bin/env python3

output = open('output').read()

values = []
for line in output.split('\n'):
    if 'LOAD_CONST' in line:
        print(line)
        v = line.split('LOAD_CONST')[1].split('(')[1].split(')')[0]
        try:
            values.append(int(v))
        except:
            values.append(v)

con = values[34:34+240]
secret = values[-6-256:-6]
print(secret)

notes = []
for i in range(len(con) // 2):
    notes.append((con[i] + con[120 + i]) // 2)
notes.append((con[119] - con[120 + 119]) // 2)

print(bytes([secret[i] ^ notes[i % len(notes)] for i in range(len(secret))]))
