#!/usr/bin/python3 -u

import codecs
import hashlib

from art import youShallNotPass
from lib import printflag


if __name__ == '__main__':
    passwd = input('Password: ')
    try:
        passwd = codecs.decode(passwd, 'hex')
        assert 16 < len(passwd) < 70
    except:
        print('Nope')
        exit(255)

    if hashlib.md5(passwd).hexdigest() != 'cd86c62d1c8d808a96e49511e0b79158':
        print(youShallNotPass)
        exit(255)

    print('Enjoy your flag :)')
    printflag(passwd)
