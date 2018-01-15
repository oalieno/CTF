# EOF CTF 2018

## writeme

輸入一個位置

程式會讀該位置的值給你並且給你寫該位置的值

就讀 puts got 的值 ( leak libc base address )

寫 puts got 的值成 one_gadget

## magicheap2

這題是程式安全練習的 [magicheap](https://csie.ctf.tw/problems/37) 的變形

一樣是 heapoverflow 但是沒有直接 cat flag 給你了

一開始一直在想用 unlink 可是還沒有 libc base address

就在一開始輸入名字的地方偽造 chunk 並且用 fastbin attack 把 read got 的最後兩個 bytes 改成 one_gadget 的最後兩個 bytes

1/16 的機率直接撞爛他XD

## singlehell

`client` 是 ELF 64 bits 的程式有 UPX 加殼 ( 先解個殼 )

程式有兩個功能

1. 攻擊怪物
2. 自己回血 ( 要耗魔有上限 )

程式本身是用 socket 連遠端的 server

重點是最一開始連上 server 的時候，server 會給一個 token

中間傳輸的訊息是用這個 token 做 xor 加密

所以就寫 script 直接把自己的攻擊調高到 `0xFFFFFFFF` 打個 232 次怪物就死了就拿到 flag 了

## helloworld

程式直接執行起來會 segmentation fault

用 `ltrace` 會發現他會先 `getenv("hel1oworld")`

然後會發現他會把 hel1oworld 這個環境變數拿去做複雜的檢查，檢查成功就輸出 `Correct:)`

看起來就是用 symbolic execution 的題目

把 IDA 反編譯出來的 code 拿去 klee 解一下就出來了

注意的是要用 `unsigned long long`
