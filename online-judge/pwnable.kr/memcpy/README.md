# pwnable.kr : memcpy

**points** : 10

## write-up

這題直接執行 binary 會 segmentation fault

就沒辦法看到最後面的 flag 了

他壞掉的原因是 `movdqa` 和 `movntps` 都需要位置是 16 bytes aligned

而 src 是固定一開始開好的是沒有問題的

重點在 dest 是用我們給的數字 malloc 出來的

所以就是考我們對 malloc heap 空間會發生什麼事

反正熟悉 heap 的就會覺得只是一塊蛋糕

只要我們給他的數字除以 8 是奇數就好 ( 因為加上 8 bytes header 剛好 aligned 16 bytes )

`echo "8 24 40 72 136 264 520 1032 2056 4104" | ./memcpy `

# other write-ups and resources

