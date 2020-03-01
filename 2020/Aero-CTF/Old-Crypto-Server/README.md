# Aero CTF 2020 : Old Crypto Server

**category** : crypto

**points** : 100

## write-up

AES ECB encrypt `msg + flag`, `msg` is controllable.

Send `msg = 'a' * 15`, and the first block will be `'a' * 15 + flag[0]`  
Then send `msg = 'a' * 15 + '0'`, `msg = 'a' * 15 + '1'`, ..., until you find a match with the previous result and you got `flag[0]`.

Send `msg = 'a' * 14`, and the first block will be `'a' * 14 + flag[0] + flag[1]`  
Then send `msg = 'a' * 14 + flag[0] + '0'`, `msg = 'a' * 14 + flag[0] + '1'`, ..., until you find a match with the previous result and got `flag[1]`

Keep going and you will find the whole flag.

See `solve.py` for more detail.

# other write-ups and resources
