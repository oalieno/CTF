# N1CTF 2018 : easy fs

**category** : crypto
**points** : 327
**solves** : 42/517

## write-up

經典的 Håstad's Broadcast Attack

不同的 N 相同的 e 相同的訊息

有提供程式執行檔

程式主要有三個功能

1. 列出檔案 (`ls -l`)
2. 讀檔案後 RSA 加密印出
3. 使用者輸入訊息後 RSA 加密印出

使用第一個功能我們可以發現有目錄底下有兩個檔案

```
-rwxr-xr-x 1 root root  16 Mar 12 15:15 a_small_file
-rwxr-xr-x 1 root root 216 Mar 12 15:15 flag
```

使用第二個功能，使用者挑選 e

如果之前有產生過 N 的話這邊不會再產生新的 N

如果之前沒有產生過 N 的話會產生新的 N，但是會把讀出的檔案攪爛 ( 一開始一直跳這個坑 )

使用第三個功能，使用者挑選 e ，程式會隨機產生新的 N

所以攻擊流程就是

1. 使用第三個功能產生 Ni，指定 e = 3 (有可能 gcd((p-1)(q-1), e) != 1 要重試一次)
2. 使用第二個功能獲得加密的 Ci

重複三次，也就是 i = 0 ~ 2

然後用 Håstad's Broadcast Attack 打完收工

flag : N1CTF{A_sm4ll_l34k_l3ad5_t0_l4rge_br34k}

## other write-ups and resources

