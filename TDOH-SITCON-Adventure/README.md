# TDOH SITCON Adventure

這是 TDOH 在 SITCON 擺攤的闖關活動 ( http://ctf.tdohacker.org/ )

原本題目的名字有中文

好麻煩啊我就按照 A,B,C... 編號下去了

## PA

每兩個數字一組(1 byte)

flag 除以 privKey 等於 publi 餘 secret

privKey 只有 4 bytes

flag 前面一定是 TDOH

就可以還原出 privKey

然後就可以解出 flag 了

## PB

google wiki 上的 google 介紹

找不同...嗯那就寫個 script 吧...

## PC

就調一調就出來了

## PD

跟 PA 差不多

反正前面一定是 TDOH

可以還原出 key

## PE

解方程式 84 個未知數

我用了兩種寫法

第一種是寫 python script 產生 matlab script 去跑

第二種是用 z3 解

( 不知道為什麼我一開始寫的 script 跑不出來

  後來參照 Inndy 大神的 script https://github.com/Inndy/TDOH-l5g-challenges
  
  才解出來 )
  
不過 matlab 還是比較快

## PF

用 stegsolve 神器解出 QR code

再回答個問題就噴 flag

## PG

這個被 sql injection 的 log

在被用 blind injection 的方法二分搜還原字串

寫個 script 把他挖到的還原出來就好了

## PH

這題真神奇

學到了新指令 : strings

可以看到這支程式出現的所有字串

然後就可以找到 flag 了
