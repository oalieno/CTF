# UIUCTF 2018 : Hastad

**category** : crypto 

**points** : 200

**solves** : 102

## write-up

他給兩個檔案

ciphertexts.txt 是一堆密文

moduli.txt 是三個 N

看題目應該是 Håstad's Broadcast Attack

但是我發現 ciphertexts 的前面幾個數字很整齊的都長得一樣

感覺是明文很短轉成數字很小

用 gmpy2.iroot 來開根號發現他們開根號都是整數

恩就拿到 flag 了

代表 m^3 沒有超過 N

# other write-ups and resources

