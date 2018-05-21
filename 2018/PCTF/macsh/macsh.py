#!/usr/bin/env python3

import os
import sys

from fmac import fmac, keygen

cwd = os.getcwd()

k0, k1 = keygen()

commands = [
    "echo",
    "tag"
]

privileged = {
    "pwd",
    "cd",
    "ls",
    "cat"
}

commands.extend(privileged)

def echo(s):
    print(s)

def encode(cmdline):
    return cmdline.encode('utf-8')

def tag(cmd, *args):
    if cmd not in privileged:
        cmdline = encode(" ".join([cmd] + list(args)))
        print(bytes.hex(fmac(k0, k1, cmdline)))
    else:
        print("macsh: tag: Permission denied")

def pwd():
    print(cwd)

def cd(newdir):
    global cwd
    if not os.path.exists(newdir) or not os.path.isdir(newdir):
        print("macsh: cd: {}: No such file or directory".format(newdir))
    else:
        cwd = newdir
        os.chdir(newdir)

def ls(path):
    if not os.path.exists(path):
        print("ls: cannot access '{}': no such file or directory".format(path))
        return
    if os.path.isdir(path):
        for e in os.listdir(path):
            print(e)
    else:
        print(path)

def cat(path):
    if not os.path.exists(path):
        print("cat: {}: No such file or directory".format(path))
    else:
        sys.stdout.write(open(path).read())

while True:
    print("|$|> ", end='', flush=True)
    mac, cmdline = input().split('<|>')
    cmd, *args = cmdline.split()
    if cmd not in commands:
        print("macsh: {}: command not found".format(cmd))
        continue
    if cmd == "tag" or bytes.hex(fmac(k0, k1, encode(cmdline))) == mac:
        eval(cmd)(*args)
    else:
        print(bytes.hex(fmac(k0, k1, encode(cmdline))))
        print("macsh: bad tag")
