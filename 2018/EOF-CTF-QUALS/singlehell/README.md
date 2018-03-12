# EOF CTF QUALS 2018 : singlehell

**category** : reverse

## write-up

`client` 是 ELF 64 bits 的程式有 UPX 加殼 ( 先解個殼 )

程式有兩個功能

1. 攻擊怪物
2. 自己回血 ( 要耗魔有上限 )

程式本身是用 socket 連遠端的 server

重點是最一開始連上 server 的時候，server 會給一個 token

中間傳輸的訊息是用這個 token 做 xor 加密

所以就寫 script 直接把自己的攻擊調高到 `0xFFFFFFFF` 打個 232 次怪物就死了就拿到 flag 了

## other write-ups and resources

