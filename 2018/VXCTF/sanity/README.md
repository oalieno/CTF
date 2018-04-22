# VXCTF 2018 : sanity

**category** : pwn

**points** : 450

**solves** : 5

## write-up

這題就 buffer overflow

保護也只有 NX

應該是 pwn 簽到題吧

就 ROP 串下去 one_gadget

leak libc 的時候記得串一個 fflush 的 gadget ( 我是直接跳回 main 再來一次 )

# other write-ups and resources

