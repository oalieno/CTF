# HITCON CTF quals 2015

## readable

只能蓋到 saved rbp 和 return address

所以要做 stack migration 增加 ROP 的長度

需要 rax = 0x3b, rdi = "/bin/sh", rsi = 0, rdx = 0

然後改 read got 的最後一個 bytes 改到 libc read 函式附近的 syscall (等於我們有 syscall 的 gadget)

但是因為他沒有給 libc 所以必須猜他的 offset

然後在用 read 改掉 read got 的時候順便 read 0x3b 設好 rax

rdi 有 gadget, rsi 和 rdx 可以用 __libc_csu_init 結尾長長的一段 gadget 設定

把東西都設好之後最後就呼叫 read plt 就是 syscall 了
