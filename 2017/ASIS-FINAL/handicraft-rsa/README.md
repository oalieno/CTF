# ASIS CTF FINAL 2017 : Handicraft RSA

**category** : crypto

**points** : 138

> Someone is developing his own [RSA system](https://asisctf.com/tasks/handicraft_rsa_e160ccfa45d529db2de93e3f4ac76abf99683277) in his very old home's basement. Prove him that this RSA system is only valid on his basement!

## write-up

他的 p-1 和 q-1 有很多質因數

用 pollard p-1 algorithm 就解完了

## other write-ups and resources

* https://github.com/ymgve/ctf-writeups/tree/master/asis2017finals/crypto-handicraft_rsa
* https://gist.github.com/niklasb/84fb894c7658f29b21fd7b7e1704f799
