# ASIS QUALS 2018 : the_early_school

**category** : crypto

**points** : 32

## write-up

這題是拼手速題 ( 我拼到了第六個解出來的XD )

他把明文每兩個 bytes 一組算 xor 接在後面當驗證碼 ( "\x05\x02" -> "\x05\x02\x07" )

他做了很多 round

所以就每三個 bytes 把最後的 byte 拔掉

做個幾輪就行了

# other write-ups and resources

