# AIS3 FINAL 2017 : pwn1

**category** : pwn

## write-up

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

## other write-ups and resources
