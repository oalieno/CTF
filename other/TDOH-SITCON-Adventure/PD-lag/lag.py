#!/usr/bin/env pyhon3

def generate_key(password='password', key=0x9487):
    assert type(password) is str
    assert type(key) is int

    for p in password:
        key *= ord(p)
        key ^= ord(p)

    return key

def cipher(data, key):
    output = []

    for i in data:
        key = (key * 0xc8763) + 9487 # key mutation
        b = (i ^ key) & 0xff # data must be one byte after encryption
        output.append(b)

    return bytes(output)

def main():
    password = input('Input encryption password: ')
    key = generate_key(password)

    with open('lag', 'rb') as Flag:
        data = Flag.read()
        assert data.startswith(b'TDOH{') and data.endswith(b'}\n')

    encrypted = cipher(data, key)

    with open('enc', 'wb') as Fenc:
        Fenc.write(encrypted)

if __name__ == '__main__':
    main()
