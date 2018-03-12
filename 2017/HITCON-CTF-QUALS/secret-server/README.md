# HITCON CTF QUALS 2017 : Secret Server

**category** : crypto

**points** : 221

> AES is unbreakable. Right?
>
> nc 52.193.157.19 9999
>
> [secretserver-03f9e1472f1088fcf5571d3288e759e3.py](https://s3-ap-northeast-1.amazonaws.com/hitcon2017qual-static/secretserver-03f9e1472f1088fcf5571d3288e759e3.py)

## write-up

### part 1 : `proof_of_work`

#### 情境

最一開始程式有一個 `proof_of_work` 的函式

隨機產生一個字串 $A$

給你 $A$ 的 SHA256 的 hash 和 $A$ 的一部分

#### 目標

還原出 $A$

#### 解

暴力嘗試所有可能即可

這一部分只是不讓你暴力一直 request

### part2 : `send_msg` & `recv_msg`

#### 情境

程式接收使用者輸入是用 `recv_msg` 這個 function

這個 function 就是讀取輸入 $input$ 後

$input$ 前 16 個 bytes 當作 IV

$input$ 16 個 bytes 以後的當作 data

key 是程式一開始就用 random 函式產生好的，**在同一次連線中相同**

作 AES CBC 解密


程式的輸出是用 `send_msg` 這個 function

這個 function 是把輸出 $output$ 當作 data

IV 固定是 `2jpmLoSsOlQrqyqE`

key 是程式一開始就用 random 函式產生好的，**在同一次連線中相同**

作 AES CBC 加密

#### 目標

能部分控制解密完的內容 (16 bytes)

#### 解

proof of work 完之後

程式會先 `send_msg('Welcome!!')`

所以我們可以完整的知道一組

plaintext, ciphertext, IV

如果我們想讓 `recv_msg` 解密完出來的 msg 改成 $message$

$IV' = plaintext \oplus IV \oplus message$

$cipher' = cipher$

`recv_msg(IV' + cipher)` $\to$ $message$

### part 3 : decrypt flag

#### 情境

能控制 msg 我們就可以拿到下面的各種 send_msg 出來的東西

```python
msg = recv_msg().strip()
if msg.startswith('exit-here'):
    exit(0)
elif msg.startswith('get-flag'):
    send_msg(flag)
elif msg.startswith('get-md5'):
    send_msg(MD5.new(msg[7:]).digest())
elif msg.startswith('get-time'):
    send_msg(str(time.time()))
elif msg.startswith('get-sha1'):
    send_msg(SHA.new(msg[8:]).digest())
elif msg.startswith('get-sha256'):
    send_msg(SHA256.new(msg[10:]).digest())
elif msg.startswith('get-hmac'):
    send_msg(HMAC.new(msg[8:]).digest())
else:
    send_msg('command not found')
```

看到 AES CBC 就會想到 oracle padding attack

但是稍微實驗一下可以發現 Crypto.Cipher 的 AES 的 encrypt, decrypt 的函式要求 input 一定要是 16 的倍數

所以都要自己 padding

而程式中的 unpad 函式是 **直接把最後一個 byte 的個數的字拿掉**

```python
def unpad(msg):
    return msg[:-ord(msg[-1])]
```

所以 padding 錯誤不會有 error

#### 目標

decrypt flag

#### 解

雖然他傳回來的東西都是加密過的

但我們可以再把他傳回來的東西再傳過去給他解密

**第一步**

我們接到加密的 flag 有 48 bytes (3 個 blocks)

C1, C2, C3 是 flag 的 ciphertext

P1, P2, P3 是 flag 的 plaintext

![](https://i.imgur.com/h6JD5Gc.png)

因為我們知道 P1 的前 7 個字是 `hitcon{`

用之前用的技巧把 IV 改掉讓 P1 的前 7 個字變成 `get-md5`


更改 C2 的最後一個 byte 從 0x00 - 0xff

這樣等於更改了 P3 的最後一個 bytes

因為 unpad 是 **直接把最後一個 byte 的個數的字拿掉**

所以當拿掉太多字也把 `get-md5` 破壞掉之後

他就會 `send_msg('command not found')`

紀錄 C2 改成哪些字可以進到 `get-md5` 推出 P3 的最後一個 byte 是 `\x10`

代表 C3 整個 block 都是 padding

```python
oks = [...] # 可以進到 get-md5 的 bytes
# i 是 iterater C3 block cipher decryption 完的最後一個 byte
for i in xrange(256):
    success = True
    for ok in oks:
        if not ( 1 <= i ^ ok <= 41 ):
            success = False
            break
    if success:
        print "P3[-1]:", i ^ C2[-1]
        break
```

**第二步**

第一輪

構造 C = C1, C2, C3, C3

一樣透過 IV 把 P1 的前 7 個 bytes 改成 `get-md5`

因為我們知道 P3 的最後一個 byte 了

所以我們可以直接控制最後一個 byte

讓 P3 最後一個 byte 改成 64-7-1 = 56

所以 unpad 完之後 msg = `get-md5?` (? 是 flag 的第八個字)

程式會 `send_msg(MD5.new(msg[7:]).digest())` 也就是 `send_msg(md5(?))` 回來給我

我就重新傳回去給他

然後去猜 `?` 是什麼

根據我猜的 `?` 產生 `md5(?)` 當作已知 plaintext

同樣改 IV 讓他前七個 bytes 變成 `get-md5`

猜中的話回傳回來的就不是 `send_msg('command not found')` 而是進到 `get-md5` 這個 `elif` 程式片段回傳某個東東回來

這樣就知道第八個字了

接著用同樣的方法就可以一個字一個字解出 flag 了

## other write-ups and resources

* https://ctftime.org/writeup/7975
* https://github.com/p4-team/ctf/tree/master/2017-11-04-hitcon/secret_server
* https://sectt.github.io/writeups/Hitcon-quals-17/crypto_Secret_server/README
