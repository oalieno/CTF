# EOF CTF QUALS 2018 : magicheap2

**category** : pwn

## write-up

這題是程式安全練習的 [magicheap](https://csie.ctf.tw/problems/37) 的變形

一樣是 heapoverflow 但是沒有直接 cat flag 給你了

一開始一直在想用 unlink 可是還沒有 libc base address

就在一開始輸入名字的地方偽造 chunk 並且用 fastbin attack 把 read got 的最後兩個 bytes 改成 one_gadget 的最後兩個 bytes

1/16 的機率直接撞爛他XD

## other write-ups and resources

