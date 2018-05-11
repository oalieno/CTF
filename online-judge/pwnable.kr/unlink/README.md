# pwnable.kr online-judge : unlink

**points** : 10

## write-up

這題就是考 heap 的 unlink

但是他的 unlink 是自己實作給我們練習的所以沒有檢查

可以利用 main function 最底下的 `mov ecx,DWORD PTR [ebp-0x4]` 和 `lea esp,[ecx-0x4]`

或者是 unlink function 最後面的 `leave`

蓋掉 saved ebp 讓我們可以控制 stack 變到 heap 上然後在對應的位置上放好 `shell` 的 address

# other write-ups and resources

