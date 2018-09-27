# csie.ctf.tw

程式安全 2017 作業紀錄

## HW3

### 題目 : readme

保護機制 :

![](https://i.imgur.com/tzm2nKW.png)

漏洞 :

buffer overflow 0x10 bytes

攻擊 :

buffer overflow 只能剛好蓋到 saved rbp 和 return address

所以需要用 stack migration 的技巧來完成 ROP

但是如果要做 ret2libc 的話要先 leak libc base address

而唯一能 leak 資訊出來的 printf 需要超過兩 pages 以上的 stack

所以我改用另一種方式

也就是雖然 libc 的位址是隨機的但是不是整個 address 都是隨機的

他的後 1.5 個 bytes 是固定的

而且 read 附近會有 syscall 這個指令

所以我們就蓋 read got 的最後一個 bytes 讓我們可以把 read plt 當作 syscall gadget

在 syscall 之前要把參數設好

用 ROPgadgets 這個工具可以找到 pop rdi ; ret 的 gadget

rdx 則是用 __libc_csu_init 這裡的 mov rdx, r13 這一大串的 gadget 作設定

rax 是用 setvbuf 附近的 mov eax, edx 先用剛剛的 gadget 把 rdx 設好在把 setvbuf got 的最後 2 bytes 改掉變成 gadget ( 有 1/16 的機率成功猜到那個 0.5 個 byte )

最後就是全部串起來用 stack migration 作 ROP 就拿到 flag 了 ( 在每次送 payload 前先 sleep(0.5) 才成功，`read` 不穩定 )

![](https://i.imgur.com/mc3PVdE.png)

![](https://i.imgur.com/cTpp41X.png)

## HW4

### 題目 : fmtfun4u

保護機制 : 

![](https://i.imgur.com/Qs0wMHA.png)

漏洞 : format string

攻擊 :

format string 一次只能 0x10 個字

而且只能寫 4 次很不方便

所以我先 leak stack base address 後把 for 迴圈中的 i 隨便改成一個很大的數字

可以視為有無限次的 format string

接下來就簡單啦

hijack malloc_hook 跳到 libc 中的 one_gadget 就完成了

### 題目 : hacknote2

保護機制 :

![](https://i.imgur.com/OCW4oOW.png)

漏洞 : use after free

攻擊 :

用 use after free 漏洞可以修改 note 的 printnote 函式和 content 指標

先改 content 指標成 puts 的 got，printnote 函式維持不變

就可以 leak libc address

再來就改 printnote 函式成 libc 裡面的 one_gadget

然後就大功告成打完收工
