# ASIS QUALS 2018 : uncle-sam

**category** : crypto

**points** : 120

## write-up

先用 [online OCR](http://www.newocr.com/) 把圖片中的數字拿出來

```
n = p * p * q
e = n
l = (p - 1) * (q - 1) // gcd(p - 1, q - 1)
d = inverse(e, l)
c = pow(m, e, n)
```

給你 `e, d, c`

賽中的時候我想到的是在 twenty years of rsa 裡面提到知道 d 可以分解 n

<img src="https://latex.codecogs.com/gif.latex?2^{ed&space;-&space;1}&space;=&space;2^{\frac{(p-1)(q-1)}{gcd(p-1,&space;q-1)}}&space;=&space;2^{k(p-1)}&space;\equiv&space;1&space;\pmod{p}" title="2^{ed - 1} = 2^{\frac{(p-1)(q-1)}{gcd(p-1, q-1)}} = 2^{k(p-1)} \equiv 1 \pmod{p}" />

<img src="https://latex.codecogs.com/gif.latex?gcd(2^{ed&space;-&space;1}&space;-&space;1,&space;n)" title="gcd(2^{ed - 1} - 1, n)" /> 會是 p 的倍數我們就分解 n 了 ( <img src="https://latex.codecogs.com/gif.latex?2^{ed&space;-&space;1}&space;-&space;1" title="2^{ed - 1} - 1" /> 直接算有點大，可以先 mod n 結果不會變 )

分解 `n = p * p * q` 之後

`m = pow(c, d, p * q)`

因為 <img src="https://latex.codecogs.com/gif.latex?c^d&space;=&space;m^{p^2&space;q&space;d}&space;=&space;m^{1&space;&plus;&space;\frac{(p&space;-&space;1)&space;(q&space;-&space;1)}{gcd(p-1,&space;q-1)}}&space;\equiv&space;m&space;\pmod{pq}" title="c^d = m^{p^2 q d} = m^{1 + \frac{(p - 1) (q - 1)}{gcd(p-1, q-1)}} \equiv m \pmod{pq}" />

看其他人 writeups 發現這題是 Schmidt-Samoa Cryptosystem

# other write-ups and resources

