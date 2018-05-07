# ASIS QUALS 2018 : Shapiro

**category** : ppc

**points** : 218

## write-up

這題是要找一個 k x k 的格子點 ( k <= 10 )

使得每個點 (x, y) 的 gcd(x, y) 不等於 1

總共有 8 關，每關會限制所有的 x 要小於或大於某個數字，或是 y 要小於或大於某個數字

我們先找一個 general solution

方陣的最左下角我們叫 (a, b)

掃個每個格子 (x, y) 從 (0, 0) 到 (10, 10)，給 x, y 一個共同的質因數 g

假設 (3, 4) 分配的共同質因數是 17 那 a % 17 = -3 且 b % 17 = -4

把所有 constrain 組起來用中國剩餘定理求 (a, b) 就找到 general solution 了

但是有些限制是 x 要小於某個數字而 general solution 太大了

因為只有 8 關，賽中我是直接不管限制直接給通解，只要我們遇到 8 關的限制都是大於某個數字就行了XD

後來看人家 writeups 發現格子點可以是負的，那就把通解減掉 mod 的乘積變成負的也會滿足

# other write-ups and resources

