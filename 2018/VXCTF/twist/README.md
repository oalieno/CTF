# VXCTF 2018 : Mersenne had a fun time twisting

**category** : crypto

**points** : 500

**solves** : 1

## write-up

這題是使用 mt19937 random number generator 產生 key 來做 xor cipher

可以看到原始碼中的 `res >> (8 * (3 - count));` 這行怪怪的 ( 應該是 `>>=` 才對 )

仔細看了一下 code 會發現 flag.out 的每四個 8 bytes 的前三個 8 bytes 可以完全還原回來原來的字 ( 8 bytes 的最後一個 byte 就是原來的字 )

但是第四個 8 bytes 完全就是被 xor 掉了而我也不知道怎麼破解 mt19937

到這裡我們的 flag 已經長這樣了 : `vxc#f{A#3_u#d01#5_1#_bY#f0r#3_o#_TH#_sM#rT_#4Y?#` ( `#` 代表我們不知道的字 )

仔細的看一下會發現他的英文應該是 : `are u doing it by force or the smart ways`

唯一不確定的就是字的大小寫或是被換成其他奇怪的字

那我就寫了一個暴力送 flag 的 script 把所有可能猜一次

然後就對了 O_O

不知道正解怎麼解的 XD

# other write-ups and resources

