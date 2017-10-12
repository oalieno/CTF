# ais3-2017-final

## Web1

/robots.txt 下有隱藏路徑，瀏覽會發現 index.php 的原始碼，flag 在上面

## Web2

這題的 server 跟 Web1 一樣，所以就去看 Web1 找到的原始碼，發現他的 cookie 是 serialize 的 object

然後我們要讓 $token == $admin_token ( 變數名稱不知道有沒有記錯 )

所以呢我們就讓 $token 是 true 就好囉 ( 因為 true == 任意非空字串 )

也就是在 serialize 的 data 中把原本的 s:10:1234567890 換成 b:1

## Misc1

執行就有 flag 了 O_O?

## Misc2

隊友解的，暴搜即可

## Misc3

他給的檔案是用 xor 加密後

再用 1 bytes = 9 bits 表達 ( 跟風今年 DEFCON CTF )

所以就先轉回來 ( 碰巧我有寫過今年 DEFCON CTF 的題目，用我之前寫的 script : [parse.py](DEFCON-2017/rubix/parse.py) )

再用網路上找的爆破 xor key 的工具 ( [xortool](https://github.com/hellman/xortool) )

## Pwn1

open read write ( orw ) 的變形

題目 : 直接給他 assembly code，他幫你 execute

目標 : 讀取 /home/pwn1/flag

條件限制 :
1. 只能用 open, read, write 這三個 syscall 之外
2. assembly code 只能 87 bytes ( 真是 87 )
3. read 的第三個參數 ( lens ) 要 < 42

寫 assembly 先 open 開檔再 read 讀檔再把結果 write 輸出到 stdout

必須要刪除不必要的 instructions

flag 大於 42 個字，雖然參數只能 < 42，不過一次讀不完就讀兩次啊

詳細請看 : [exploit.py](ais3-2017-final/Pwn1/exploit.py)
