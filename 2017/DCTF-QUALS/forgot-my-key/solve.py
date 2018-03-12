#!/usr/bin/env python

def minus(x,y):
    return (x + 126 - y) % 126

def set_value(encrypt,key,known,index,plain):
    key[index % 32] = minus(encrypt[index],ord(plain))
    known[index % 32] = True

encrypt = "5616f5962674d26741d2810600a6c5647620c4e3d2870177f09716b2379012c342d3b584c5672195d653722443f1c39254360007010381b721c741a532b03504d2849382d375c0d6806251a2946335a67365020100f160f17640c6a05583f49645d3b557856221b2"
encrypt = [ int(encrypt[i+1]+encrypt[i],16) for i in xrange(0,len(encrypt),2)]
secret = encrypt[0]
encrypt = encrypt[1:]
for i in xrange(len(encrypt)-1,0,-1): encrypt[i] = minus(encrypt[i],encrypt[i-1])
encrypt[0] = minus(encrypt[0],secret)

key = [0] * len(encrypt)
known_key = [False] * len(encrypt)
message = [0] * len(encrypt)

set_value(encrypt,key,known_key,0,'D')
set_value(encrypt,key,known_key,1,'C')
set_value(encrypt,key,known_key,2,'T')
set_value(encrypt,key,known_key,3,'F')
set_value(encrypt,key,known_key,4,'{')
set_value(encrypt,key,known_key,len(encrypt)-32-2,'}')
set_value(encrypt,key,known_key,len(encrypt)-32-1,'|')

for _ in xrange(10):
    for index,word in enumerate(encrypt):
        index_key = index % 32
        if not known_key[index_key]: continue
        message[index] = minus(encrypt[index],key[index_key])
        if len(encrypt)-32 <= index:
            now = 32-len(encrypt)+index
            if known_key[now] and key[now] != message[index]:
                raise Exception
            key[now] = message[index]
            known_key[now] = True
print "".join(map(chr,message))
