# N1CTF 2018 : losetome

**category** : ppc
**points** : 153
**solves** : 111/517

## write-up

這題的 proof of work 是要用 [hashcash](http://www.hashcash.org/tool/linux/) 算東東

然後就要跟電腦玩黑白棋 (reversi 或叫 othello)

但是這不是一般的黑白棋，一般的黑白棋是比賽結束時有最多子的人贏

這是 misere 版本的黑白棋，也就是比賽結束時有最少子的人贏

這時候就要發揮 google 搜尋的功力了

使用關鍵字 `anti reversi github` 找到這個 [repo](https://github.com/sum2012/sum-gnu-anti-Reversi-delphi-windows)

然後用他打爛主辦單位的 AI 拿到 flag

## other write-ups and resources

