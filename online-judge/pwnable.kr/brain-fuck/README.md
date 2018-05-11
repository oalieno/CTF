# pwnable.kr : brain-fuck

**points** : 150

## write-up

這題是用 c 實作的 brainfuck

因為 brainfuck 本身就是在操作指標

所以我們可以讀寫任意位置

不過這個 brainfuck 沒有實作 `[]` 所以沒有迴圈可以用

然後 input 限制 1024 指標 `p` 一次只能 +1 或 -1 所以還是不能走太遠

exploit 的流程我在 `exploit.py` 寫的很清楚了

1. leak libc base address through setvbuf got
2. setvbuf got = system
3. putchar got = main
4. stdout = buf
5. buf = "sh\x00"

剛好 setvbuf 的第一個參數是 stdout, stdin 在 got 附近可以蓋掉

這樣我們就可以把 setvbuf 換成 system 然後操控 system 的第一個參數為 "sh\x00"

# other write-ups and resources

