# ASIS CTF FINAL 2017 : Dig Dug

**category** : web

**points** : 29

> The pot calling the [kettle](https://digx.asisctf.com/) black.

## write-up

`dig digx.asisctf.com` 找 ip

`dig -x 192.81.223.250` dns 反查 domain name

找到一個新的 domain name -> airplane.asisctf.com

去瀏覽發現一個神秘的 `./js.js`，然後在 browser console 執行 `./js.js`

會印出主辦單位給的好心提示 ( 就是說要開飛航模式才看的到 flag )

\> window.help()

\> window.dispatchEvent(new Event('offline'))

噴 flag

## other write-ups and resources

* https://rawsec.ml/en/ASIS-2017-Final-write-ups/#dig-dug-web
* https://ctftime.org/writeup/7445
* https://github.com/occupe/Writeups-CTF/blob/master/ASIS-CTF/Dig%20Dug/Readme.md
* http://2amresearch.com/?p=18
* https://github.com/ymgve/ctf-writeups/tree/master/asis2017finals/web-dig_dug
