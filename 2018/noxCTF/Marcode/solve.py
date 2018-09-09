#!/usr/bin/env python3
import hashlib
import string

dictionary = {
    'A': '000013',
    'B': '000396',
    'C': '000463',
    'D': '000467',
    'E': '000453',
    'F': '000648',
    'G': '000660',
    'H': '000675',
    'I': '000683',
    'J': '001481',
    'K': '001793',
    'L': '002814',
    'M': '003217',
    'N': '003125',
    'O': '003172',
    'P': '002807',
    'Q': '000110',
    'R': '002660',
    'S': '003185',
    'T': '003171',
    'U': '002817',
    'V': '003316',
    'W': '002383',
    'X': '002193',
    'Y': '003239',
    'Z': '000176',
    '_': '003230',
    '?': '003229'
}

lookup = {}
for k, v in dictionary.items():
    filename = 'pictures/{}.png'.format(v)
    with open(filename, 'rb') as data:
        f = data.read()
        h = hashlib.sha1(f).hexdigest()
        lookup[h] = k

flag = ''

for i in range(1, 3491):
    filename = 'pictures/{:0>6}.png'.format(i)
    with open(filename, 'rb') as data:
        f = data.read()
        h = hashlib.sha1(f).hexdigest()
        flag += lookup[h]

print(flag)
