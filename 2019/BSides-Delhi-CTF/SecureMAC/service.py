#!/usr/bin/python
from Crypto.Cipher import AES
from Crypto.Util.strxor import strxor
from binascii import hexlify, unhexlify
from Crypto.Util.number import *
from secret import key, flag
import sys

def sign(key, message):
	try:
		ECB = AES.new(key, AES.MODE_ECB)
		messageblocks = [message[i:i + 16] for i in range(0, len(message), 16)]
		tag = ECB.encrypt(messageblocks[0])
		for i in range(1,len(messageblocks)):
			tag = ECB.encrypt(strxor(messageblocks[i], tag))
		return hexlify(tag)
	except:
		sys.exit()

if __name__ == '__main__':
	print("Are you sure you can break this??")
	p = getPrime(512)
	q = getPrime(512)
	n = p*q
	e = 65537

	enc_key = pow(bytes_to_long(key),e,n)
	c1 = pow(bytes_to_long("fake_flag"),e,p)
	c2 = (pow(bytes_to_long("fake_flag"),e,q) ^ 1337)%q
	qinv = inverse(q,p)
	h = (qinv * (c1 - c2)) % p
	c = c2 + h*q
	print("n: " + str(n))
	print("c: " + str(c))
	print("enc_key: " + str(enc_key))

	while(True):
		try:
			msg1 = unhexlify(raw_input("\nMessage 1: \n"))
			msg2 = unhexlify(raw_input("\nMessage 2: \n"))
                        print "input recieved"
			if(msg1 == msg2):
				print("Not so easy to fool")
				sys.exit()
			if(msg1 != msg2 and sign(key, msg1)==sign(key, msg2)):
				print("Congrats!! Here's your flag: " + flag)
				sys.exit()
			else:
				print("\nTags don't match")
				sys.exit()
		except:
			sys.exit()
