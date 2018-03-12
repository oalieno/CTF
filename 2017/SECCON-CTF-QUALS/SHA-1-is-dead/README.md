# SECCON CTF QUALS 2017 : SHA-1 is dead

**category** : crypto

**points** : 100

> SHA-1 is dead http://sha1.pwn.seccon.jp/ Upload two files satisfy following conditions:
>
> file1 != file2
>
> SHA1(file1) == SHA1(file2)
>
> SHA256(file1) <> SHA256(file2)
>
> 2017KiB < sizeof(file1) < 2018KiB
>
> 2017KiB < sizeof(file2) < 2018KiB
>
> 1KiB = 1024 bytes

## write-up

SHA1 collision 但是要求兩個檔案的大小要介於 2017KiB ~ 2018KiB

那就把 google 的那兩個檔案拿來後面隨便接一些一樣的字串讓大小夠就好了

flag : SECCON{SHA-1_1995-2017?}

## other write-ups and resources

* http://blog.terrynini.tw/en/2017-SECCON-Write-up/
* http://dongdd.tistory.com/82
