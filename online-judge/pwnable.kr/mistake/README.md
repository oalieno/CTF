# pwnable.kr : mistake

**points** : 1

## write-up

`>` 的 operator precedence 比 `=` 還要大

所以 `if(fd=open("/home/mistake/password",O_RDONLY,0400) < 0)` 其實是 `if(fd = (open("/home/mistake/password",O_RDONLY,0400) < 0))`

也就是 fd = 0 ( stdin )

所以其實 password 是我們自己可以輸入的

那我們就先輸入 `bbbbbbbbbb`

然後再輸入 `cccccccccc` ( 每個字元 xor 1 就是上面的密碼 )

就有了

# other write-ups and resources

