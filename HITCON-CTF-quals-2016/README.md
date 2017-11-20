# HITCON CTF Quals 2016

## lets-decrypt

AES CBC mode 加密

flag 就是 `hitcon{IV}`

他提供一個功能可以讓你任意解密得到結果 (用同樣的 IV 和 key)

餵給他 C2 + C2 + C3 可以成功拿到 IV...

## hackpad

給一個 PCAP 檔
用 strings 這個指令把有 msg 的都抓出來

```
msg=0000000000000000000000000000d903997d9369c74c82abba4cc3b1bfc65f02
md5(decrypt(msg)) = 9f5b543c64d3e384078fdd8cf4b2ce6d
```

strings 出來的結果像上面這樣

第一行是說給 msg=xxx 然後 server 去解密

然後 server 會回傳 200 OK 和 decrypt 完的 md5

或是 500 error 然後沒有訊息 (padding error)

最開始的 `msg=3ed2e01c...` 是加密過得密文，裡面藏有 flag

攻擊者正在做 oracle padding attack

所以應該是 AES CBC 加密

他一次猜一個 block

他都幫我們猜好了

我們只要去找他猜到的東西把他轉回來就好了

```
msg=67acd06f7f7b28762310ce1213fccb11997d9369c74c82abba4cc3b1bfc65f02
md5(decrypt(msg)) = d41d8cd98f00b204e9800998ecf8427e
```

比如這兩行

他猜完了一個 block (前面沒有 0)

![](https://i.imgur.com/VlaaJLn.png)

根據 oracle padding attack 的原理回推

![](https://i.imgur.com/sWK9OVo.png)

然後把所有的東西都解出來 flag 就在最後面 ([solve.py](forensics/hackpad/solve.py))

## handcrafted-pyc

這題給你的是編譯成 python byte code 的 python code

[marshal](https://docs.python.org/2/library/marshal.html) 是用來把 python object 打包成 binary 的工具

用 `marshal.loads` 變回來的是一個 code object (這其實用內建 [compile](https://www.programiz.com/python-programming/methods/built-in/compile) function 出來的是一樣的)

那我們先用 python 的 dis 函式庫做 disassembly ([generate.py](reverse/handcrafted-pyc/generate.py))

觀察一下可以看到很多的 LOAD_CONST ([disassembly-code](reverse/handcrafted-pyc/disassembly-code))

把所有的 LOAD_CONST 後面的數字轉回字母就會變 ([solve2.py](reverse/handcrafted-pyc/solve2.py))

```
llaC em yP aht notriv lauhcamni !eac Ini npreterP tohty ntybdocese!!!ctihN{noy woc uoc naipmoa eldnur yP nnohttyb doceni euoy rb ria}!napwssro :dorWp gnssadrow...elP  esa yrtaga .ni oD tonurbf etecro)= .
```

稍微觀察一下規律就可以找回 flag 了

另一個作法是去看他 disassembly 出來的 code

把 `750 LOAD_FAST                0 (password)` 這行插到 `2212 PRINT_ITEM` 之前 ([solve.py](reverse/handcrafted-pyc/solve.py))

就可以直接印出密碼

在帶回去 crackme.py 就有 flag 了
