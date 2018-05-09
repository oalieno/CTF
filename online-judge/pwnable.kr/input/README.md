# pwnable.kr : input

**points** : 4

## write-up

ssh 到 server 後

```
-r--r-----  1 input2_pwn root      55 Jun 30  2014 flag
-r-sr-x---  1 input2_pwn input2 13250 Jun 30  2014 input
-rw-r--r--  1 root       root    1754 Jun 30  2014 input.c
```

而 input 有 5 關

我們過了五關後 input 就會 cat flag 給我們

我一開始是用 python3 + xargs 去過前兩關

```
python3 -c 'import os; import sys; sys.stdout.buffer.write(b"\x00\x0a\x00\xff" + b"\x00\x0a\x02\xff"); os.environ[b"\xde\xad\xbe\xef"] = b"\xca\xfe\xba\xbe"' | xargs --null -a <(python3 -c 'import sys; sys.stdout.buffer.write(b"\x00".join([b"a"] * 64) + b"\x00\x00\x20\x0a\x0d\x00" + b"\x00".join([b"a"] * 33))') ./input 2>&0
```

不過 stage 3 的環境變數就弄不太起來

然後發現我們可以在 /tmp 底下開自己的資料夾在裡面寫檔

所以我就寫了個 C 把前面幾關過了最後在 `execv` 成 `input`，建個 symbolic link 過來

stage 5 的 socket 我是直接用 python3 + nc 去做的，因為用 C 寫 socket 好麻煩 XD

# other write-ups and resources

* https://www.jianshu.com/p/e13f3bc26cd4
