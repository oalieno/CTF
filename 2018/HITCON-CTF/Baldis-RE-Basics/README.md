# HITCON CTF 2018 : Baldis-RE-Basics

**category** : misc

**points** : 421

**solves** : 3

## write-up

In this challenge, we have to do **assemble, disassemble, and emulate** for 8 kinds of architecture

Here is the list of packages I used to solve this challenge

| architecture | assemble | disassemble | emulate |
| --- | --- | --- | --- |
| i386 | pwntools | capstone | unicorn |
| amd64 | pwntools | capstone | unicorn |
| arm | pwntools | capstone | unicorn |
| aarch64 | pwntools | capstone | unicorn |
| mips | keystone | capstone | unicorn |
| powerpc | pwntools | capstone | pwntools.run_shellcode ( qemu ) |
| risc-v | pwntools-patch | pwntools-patch | pwntools-patch.run_shellcode ( [spike](https://github.com/riscv/riscv-isa-sim) )  |
| wasm | wabt/wat2wasm | [wasm](https://github.com/athre0z/wasm) | wabt/wasm-interp |

There are 7 rooms at the beginning

Every room will contain a random architecture to solve

After solving 7 rooms, the hidden architecture **wasm** will come up = =

![](https://i.imgur.com/QaXisdl.png)

### install

First, we need to install lots of package

binutils for different architecture

```
apt-get install binutils-powerpc-linux-gnu \\
                binutils-aarch64-linux-gnu \\
                binutils-mips-linux-gnu \\
                binutils-arm-linux-gnueabi
```

[keystone](http://www.keystone-engine.org/) to assemble

[capstone](http://www.capstone-engine.org/) to disassemble

[unicorn](https://www.unicorn-engine.org/) to emulate

also the mighty **pwntools** which can do everything

[riscv-tools](https://github.com/riscv/riscv-tools) for risc-v architecture ( compile this need lots of time, remember to set multithread flag `-j8` )

[wabt](https://github.com/WebAssembly/wabt) for wasm architecture

### assemble

For assemble, we need to **assemble** assembly code to machine code

**pwntools** is enough for most architecture

However, pwntools `asm` for **mips** didn't get the right answer. Use keystone instead

### disassemble

For disassemble, we need to **disassemble** machine code to assembly code

At first, I also use **pwntools** for disassemble, and use regex replace to fix the format

Then, one of my teammate realize that the server use **capstone** to do disassemble

### emulate

For emulate, the server will give us a **function**, and we need to determine the right answer for the **return value** after the function is executed.

**unicorn** is easy to use, because it can read a register out directly from script

**unicorn** did not support powerpc, so we use **pwntools** `run_shellcode` function, which actually use qemu, to emulate shellcode for us

`run_shellcode` only give us **exit code** ( 1 byte ), I leak the return value through **exit code** and shift 8 four times to get the whole 32 bits answer.

### risc-v

**keystone**, **capstone**, **unicorn** and **pwntools** all did not support risc-v, so I patch **pwntools** `pwnlib/context/__init__.py`, `pwnlib/asm.py`, and `pwnlib/tubes/process.py` and use **pwntools** to do `asm`, `disasm`, and `run_shellcode`

I use the same trick to get the return value through **exit code**

Notice that there is a infinite loop in the shellcode ( maybe some kind of joke from the challenge maker ? )

`f0: 0000006f j 0xf0`

We need to strip the shellcode after this line to finish execution

### wasm

And finally, after 7 architectures ( and get half of the flag ) is the final hidden architecture

We use [wabt](https://github.com/WebAssembly/wabt) tools

For emulate, I wrap the disassembled shellcode inside a function and re-assemble it back to wasm and use `wasm-interp` to emulate

```
(module
  (export "square" (func $square))
  (func $square (param) (result i32)
    shellcode...
  )
)
```

flag : `hitcon{U_R_D4_MA5T3R_0F_R3_AND_PPC_!#3}`

## other write-ups and resources
