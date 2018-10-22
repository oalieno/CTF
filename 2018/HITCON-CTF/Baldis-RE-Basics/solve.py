#!/usr/bin/env python3
from pwn import *
from keystone import *
from capstone import *
from unicorn import *
from unicorn.x86_const import *
from unicorn.arm_const import *
from unicorn.arm64_const import *
from unicorn.mips_const import *
from base64 import b64encode, b64decode
from wasm.decode import decode_bytecode
from wasm.formatter import format_instruction
from wasm.opcodes import INSN_ENTER_BLOCK, INSN_LEAVE_BLOCK
import random

context.log_level = 'error'

table = {
    b' .----------------.  .----------------.  .----------------.  .----------------. \n': 'mips',
    b'                     .----.                                                      _____      \n': 'amd64',
    b' \xe2\x96\x84\xe2\x96\x84\xe2\x96\x84\xe2\x96\x84\xe2\x96\x84\xe2\x96\x84\xe2\x96\x84\xe2\x96\x84\xe2\x96\x84\xe2\x96\x84\xe2\x96\x84  \xe2\x96\x84\xe2\x96\x84\xe2\x96\x84\xe2\x96\x84\xe2\x96\x84\xe2\x96\x84\xe2\x96\x84\xe2\x96\x84\xe2\x96\x84\xe2\x96\x84\xe2\x96\x84  \xe2\x96\x84\xe2\x96\x84\xe2\x96\x84\xe2\x96\x84\xe2\x96\x84\xe2\x96\x84\xe2\x96\x84\xe2\x96\x84\xe2\x96\x84\xe2\x96\x84\xe2\x96\x84  \xe2\x96\x84\xe2\x96\x84\xe2\x96\x84\xe2\x96\x84\xe2\x96\x84\xe2\x96\x84\xe2\x96\x84\xe2\x96\x84\xe2\x96\x84\xe2\x96\x84\xe2\x96\x84  \xe2\x96\x84\xe2\x96\x84\xe2\x96\x84\xe2\x96\x84\xe2\x96\x84\xe2\x96\x84\xe2\x96\x84\xe2\x96\x84\xe2\x96\x84\xe2\x96\x84\xe2\x96\x84 \n': 'powerpc',
    b' ___   _______   _____   ___     \n': 'i386',
    b'      _       _______     ____    ____  \n': 'arm',
    b'   ____       ____     ______       ____   __    __     ______   _   _     \n': 'aarch64',
    b'  _____  _____  _____  _____   __      __\n': 'riscv64'
}

UCS = {
    'i386':    (UC_ARCH_X86, UC_MODE_32),
    'amd64':   (UC_ARCH_X86, UC_MODE_64),
    'arm':     (UC_ARCH_ARM, UC_MODE_ARM),
    'aarch64': (UC_ARCH_ARM64, UC_MODE_ARM),
    'mips':    (UC_ARCH_MIPS, UC_MODE_MIPS32 + UC_MODE_BIG_ENDIAN),
}

CPS = {
    'i386':     (CS_ARCH_X86, CS_MODE_32),
    'amd64':    (CS_ARCH_X86, CS_MODE_64),
    'arm':      (CS_ARCH_ARM, CS_MODE_ARM),
    'aarch64':  (CS_ARCH_ARM64, CS_MODE_LITTLE_ENDIAN),
    'mips':     (CS_ARCH_MIPS, CS_MODE_MIPS64 + CS_MODE_BIG_ENDIAN),
    'powerpc':    (CS_ARCH_PPC, CS_MODE_32 + CS_MODE_BIG_ENDIAN)
}

def init(r):
    r.sendlineafter('Press the Enter key to start the game', '')
    r.sendlineafter('(Press the Enter key to continue...)', '')
    r.sendlineafter('(Press the Enter key to continue...)', '')
    r.sendlineafter('Choice: ', 'A')
    r.sendlineafter('(Press the Enter key to continue...)', '')
    r.sendlineafter('Choice: ', 'B')
    r.sendlineafter('(Press the Enter key to continue...)', '')
    r.sendlineafter('Answer: ', '')

def walk(r, steps):
    for step in steps:
        r.sendlineafter('w/a/s/d:', step)

def getArch(r):
    r.recvline()
    head = r.recvline()
    try:
        return table[head]
    except KeyError:
        print(head)
        r.interactive()
        exit()

def wasmdis(machine):
    assembly = ''
    raw = bytearray(machine)
    indent = 0
    for cur_insn in decode_bytecode(machine):
        if cur_insn.op.flags & INSN_LEAVE_BLOCK:
            indent -= 1
        assembly += '  ' * indent + format_instruction(cur_insn) + '\n'
        if cur_insn.op.flags & INSN_ENTER_BLOCK:
            indent += 1
    assembly = assembly.strip()
    return assembly

def challenge1(r, arch):
    r.sendlineafter('Press the Enter key to start the challenge...', '')
    r.recvline()
    assembly = r.recvuntil('Answer:')
    assembly = assembly[:assembly.rfind(b'\n')]

    if arch == 'mips':
        ks = Ks(KS_ARCH_MIPS, KS_MODE_MIPS64 + KS_MODE_BIG_ENDIAN)
        machine, _ = ks.asm(assembly)
        machine = bytes(machine)[:-4]
    elif arch == 'wasm':
        template = '''(module
          (func $i (import "imports" "imported_func") (param i32))
          (func (export "exported_func")
          {}
          )
        )'''
        assembly = template.format(assembly.strip(b'end').strip().decode())
        filename = f'tmp/{random.randint(0, 100000)}'
        open(f'{filename}.wast', 'w').write(assembly)
        os.system(f'/root/wabt/bin/wat2wasm {filename}.wast -o {filename}.wasm')
        machine = open(f'{filename}.wasm', 'rb').read()[73:]
    else:
        machine = asm(assembly.decode(), arch = arch)
 
    r.sendline(b64encode(machine))

def challenge2(r, arch):
    r.recvline()
    machine = b64decode(r.recvline().strip())
  
    if arch == 'riscv64':
        assembly = disasm(machine, arch = arch)
        assembly = '\n'.join(map(lambda x: x[0], re.findall(' *[0-9a-f]+: *[0-9a-f]+ *([^#\n]*)(#.*)?', assembly)))
        assembly = re.sub('([^ ]*) *(.*)', '\\1 \\2', assembly)
        assembly = assembly.replace(',', ', ')
        assembly = assembly.replace(' \n', '\n')
        assembly = assembly.strip()
    elif arch == 'wasm':
        assembly = wasmdis(machine)
    else:
        cs = Cs(*CPS[arch])
        assembly = ''
        for i in cs.disasm(machine, 0x1000):
            assembly += f"{i.mnemonic} {i.op_str}\n"
        assembly = assembly.strip()

    assembly = b64encode(assembly.encode())
    r.sendlineafter('Answer:', assembly)

def challenge3(r, arch):
    r.recvuntil('What is ')
    shellcode = r.recvuntil(' ?\nAnswer:').strip(b' ?\nAnswer:')

    if arch not in ['powerpc', 'riscv64', 'wasm']:
        ADDRESS = 0x2000
        STACK   = 0x0000
        mu = Uc(*UCS[arch])
        mu.mem_map(ADDRESS, 0x1000)
        mu.mem_map(STACK, 0x1000)

    if arch == 'i386':
        shellcode = shellcode[:-1]
        mu.mem_write(ADDRESS, shellcode)
        mu.reg_write(UC_X86_REG_ESP, STACK + 0x500)
        mu.emu_start(ADDRESS, ADDRESS + len(shellcode))
        eax = mu.reg_read(UC_X86_REG_EAX)
        r.sendline(hex(eax))
    elif arch == 'amd64':
        shellcode = shellcode[:-1]
        mu.mem_write(ADDRESS, shellcode)
        mu.reg_write(UC_X86_REG_RSP, STACK + 0x500)
        mu.emu_start(ADDRESS, ADDRESS + len(shellcode))
        rax = mu.reg_read(UC_X86_REG_RAX)
        r.sendline(hex(rax))
    elif arch == 'arm':
        shellcode = shellcode[:-4]
        mu.mem_write(ADDRESS, shellcode)
        mu.reg_write(UC_ARM_REG_SP, STACK + 0x500)
        mu.emu_start(ADDRESS, ADDRESS + len(shellcode))
        r0 = mu.reg_read(UC_ARM_REG_R0)
        r.sendline(hex(r0))
    elif arch == 'mips':
        shellcode = shellcode[:-4]
        mu.mem_write(ADDRESS, shellcode)
        mu.reg_write(UC_MIPS_REG_SP, STACK + 0x500)
        mu.emu_start(ADDRESS, ADDRESS + len(shellcode))
        v0 = mu.reg_read(UC_MIPS_REG_V0)
        r.sendline(hex(v0))
    elif arch == 'aarch64':
        shellcode = shellcode[:-4]
        mu.mem_write(ADDRESS, shellcode)
        mu.reg_write(UC_ARM64_REG_SP, STACK + 0x500)
        mu.emu_start(ADDRESS, ADDRESS + len(shellcode))
        x0 = mu.reg_read(UC_ARM64_REG_X0)
        r.sendline(hex(x0))
    elif arch == 'powerpc':
        assembly = '''
        li  r0,1
        li  r1,{}
        srw r3, r3, r1
        sc
        '''
        answer = 0
        for i in range(0, 4):
            leak = asm(assembly.format(i * 8), arch = 'powerpc', endianness = 'big')
            code = shellcode[:-3] + leak
            p = run_shellcode(code, arch = 'powerpc')
            p.wait_for_close()
            byte = p.poll()
            answer = answer + byte * (256 ** i)
        r.sendline(hex(answer))
    elif arch == 'riscv64':
        ass = disasm(shellcode, arch = 'riscv64')
        ass = ass.split('\n')
        for index, line in enumerate(ass):
            if 'j' in line:
                trash = len(ass) - index
        assembly = '''
        li        a1, 0
        li        a2, 0
        li        a3, 0
        li        a7, 93
        srli      a0, a0, {}
        ecall
        '''
        answer = 0
        for i in range(0, 4):
            leak = asm(assembly.format(i * 8), arch = 'riscv64')
            code = shellcode[:-4 * trash] + leak
            p = run_shellcode(code, arch = 'riscv64')
            p.wait_for_close()
            byte = p.poll()
            answer = answer + byte * (256 ** i)
        r.sendline(hex(answer))
    elif arch == 'wasm':
        assembly = wasmdis(b'A' + shellcode)
        code = '''(module
  (export "square" (func $square))
  (func $square (param) (result i32)
{}
  )
)'''
        code = code.format(assembly.strip('end').strip())
        filename = f'tmp/{random.randint(0, 1000000)}'
        open(f'{filename}.wast', 'w').write(code)
        os.system(f'/root/wabt/bin/wat2wasm {filename}.wast -o {filename}.wasm')
        os.system(f'/root/wabt/bin/wasm-interp {filename}.wasm --run-all-exports > {filename}.out')
        answer = open(f'{filename}.out', 'r').read()
        answer = answer.split(':')[1].strip()
        r.sendline(answer)

def main():
    r = remote('13.231.83.89', 30262)

    init(r)

    routes = ['w' * 5,
              'a' * 15 + 'w',
              'd' * 5 + 's' * 4 + 'a',
              's' * 4 + 'a' * 5 + 's',
              'd' * 14 + 's',
              'd' * 16 + 's',
              'w' * 9]
    for route in routes:
        walk(r, route)
        arch = getArch(r)
        print('arch =', arch)
        challenge1(r, arch)
        challenge2(r, arch)
        challenge3(r, arch)

    r.send('\n' * 3)
    for route in routes:
        walk(r, route)
        print(r.sendlineafter('Press the Enter key to continue...', '').decode())
    walk(r, 's' * 3 + 'd' * 5)
    r.send('\n' * 3)

    arch = 'wasm'
    print('arch =', arch)
    challenge1(r, arch)
    challenge2(r, arch)
    challenge3(r, arch)

    r.interactive()

main()
