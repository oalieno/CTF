# HITCON CTF Quals 2016

## handcrafted-pyc

這題給你的是編譯成 python byte code 的 python code

[marshal](https://docs.python.org/2/library/marshal.html) 是用來把 python object 打包成 binary 的工具

用 `marshal.loads` 變回來的是一個 code object (這其實用內建 [compile](https://www.programiz.com/python-programming/methods/built-in/compile) function 出來的是一樣的)

那我們先用 python 的 dis 函式庫做 disassembly ([generate.py](HITCON-CTF-quals-2016/reverse/handcrafted-pyc/generate.py))

觀察一下可以看到很多的 LOAD_CONST ([disassembly-code](HITCON-CTF-quals-2016/reverse/handcrafted-pyc/disassembly-code))

把所有的 LOAD_CONST 後面的數字轉回字母就會變 ([solve2.py](HITCON-CTF-quals-2016/reverse/handcrafted-pyc/solve2.py))

```
llaC em yP aht notriv lauhcamni !eac Ini npreterP tohty ntybdocese!!!ctihN{noy woc uoc naipmoa eldnur yP nnohttyb doceni euoy rb ria}!napwssro :dorWp gnssadrow...elP  esa yrtaga .ni oD tonurbf etecro)= .
```

稍微觀察一下規律就可以找回 flag 了

另一個作法是去看他 disassembly 出來的 code

把 `750 LOAD_FAST                0 (password)` 這行插到 `2212 PRINT_ITEM` 之前 ([solve.py](HITCON-CTF-quals-2016/reverse/handcrafted-pyc/solve.py))

就可以直接印出密碼

在帶回去 crackme.py 就有 flag 了
