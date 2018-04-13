# 0CTF QUALS 2016 : RSA

**category** : crypto

**points** : 2

## write-up

這題有點像 rabin 的變形

e = 3 跟 phi(n) 不互質，因此不能計算出私鑰 d 來解密

而 n 有三個質因數 `n = p * q * r`

跟 rabin 的解法類似，我們就是做 m 對 p, q, r 的模開三方

然後再用中國剩餘定理把他們拼在一起

模開三方的方法可以看這篇 [New Cube Root Algorithm Based on
Third Order Linear Recurrence Relation in Finite Field](http://eprint.iacr.org/2013/024.pdf)

或者可以直接用超神的 wolframalpha

http://www.wolframalpha.com/input/?i=x%5E3+%3D+20827907988103030784078915883129+(mod+26440615366395242196516853423447))

# other write-ups and resources

* https://github.com/p4-team/ctf/tree/master/2016-03-12-0ctf/rsa
* http://mslc.ctf.su/wp/0ctf-2016-quals-rsa-crypto-2-pts/
