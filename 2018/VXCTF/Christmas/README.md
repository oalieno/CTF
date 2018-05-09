# VXCTF 2018 : Christmas

**category** : pwn

## write-up

這題就直接 `gets` 有 buffer overflow

但是沒有給 libc 而且 libc-database 也查不到是哪一個 libc

所以就來練習一下 return to dl_resolve

蓋 link_map 裡面的 l_info[DT_STRTAB] 成自己偽造的結構

然後放上 "system" 讓他解 symbol 解出 system 並呼叫

# other write-ups and resources

