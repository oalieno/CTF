# EOF CTF QUALS 2018 : helloworld

**category** : reverse

## write-up

程式直接執行起來會 segmentation fault

用 `ltrace` 會發現他會先 `getenv("hel1oworld")`

然後會發現他會把 hel1oworld 這個環境變數拿去做複雜的檢查，檢查成功就輸出 `Correct:)`

看起來就是用 symbolic execution 的題目

把 IDA 反編譯出來的 code 拿去 klee 解一下就出來了

注意的是要用 `unsigned long long`

## other write-ups and resources

