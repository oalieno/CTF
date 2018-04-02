# 0CTF QUALS 2018 : udp

**category** : reverse

**points** : 305

**solves** : 26

## notice

原本的 binary 太大了我就不放了O_O

## write-up

這個程式 fork 4000 個 process

每個 process 都監聽一個 port

![](https://i.imgur.com/7TaNWzI.jpg)

整個流程長這樣

可以用 gdb dump 出那張表 `dump memory data 0x6020e0 0x80140e0`

可以想像成每個 process 有一個點

每個點和其他點都有流量和剩餘流量

0 是起點 1 是終點

想了一想答案就是

起點 ( 0 ) 到所有人和所有人到終點( 1 ) 中比較小的那個瓶頸

# other write-ups and resources

