import os
import pickle
import random
from base64 import b64decode, b64encode
from Crypto.Util import Counter
from Crypto.Cipher import Blowfish
from secret import FLAG

p = open('user.pickle','rb').read()

key = os.urandom(8)
iv = random.randint(0, 2**64)

ctr = Counter.new(64, initial_value=iv, little_endian=True)
cipher = Blowfish.new(key, Blowfish.MODE_CTR, counter=ctr)

TOKEN = cipher.encrypt(p)

print('''
                         .
                          A       ;
                |   ,--,-/ \---,-/|  ,
               _|\,'. /|      /|   `/|-.
           \`.'    /|      ,            `;.
          ,'\   A     A         A   A _ /| `.;
        ,/  _              A       _  / _   /|  ;
       /\  / \   ,  ,           A  /    /     `/|
      /_| | _ \         ,     ,             ,/  \ 
     // | |/ `.\  ,-      ,       ,   ,/ ,/      \/ 
     / @| |@  / /'   \  \      ,              >  /|    ,--.
    |\_/   \_/ /      |  |           ,  ,/        \  ./' __:..
    |  __ __  |       |  | .--.  ,         >  >   |-'   /     `
  ,/| /  '  \ |       |  |     \      ,           |    /
 /  |<--.__,->|       |  | .    `.        >  >    /   (
/_,' \\  ^  /  \     /  /   `.    >--            /^\   |
      \\___/    \   /  /      \__'     \   \   \/   \  |
       `.   |/          ,  ,                  /`\    \  )
         \  '  |/    ,       V    \          /        `-\ 
          `|/  '  V      V           \    \.'            \_
           '`-.       V       V        \./'\ 
               `|/-.      \ /   \ /,---`\ 
                /   `._____V_____V'
                           '     '
''')

print("Your token:", b64encode(TOKEN).decode(), end="\n\n")
username = input('username : ')
password = input('password : ')
TOKEN    = input("TOKEN : ")

ctr = Counter.new(64, initial_value=iv, little_endian=True)
cipher = Blowfish.new(key, Blowfish.MODE_CTR, counter=ctr)
print()
try :
    objs = pickle.loads(cipher.decrypt(b64decode(TOKEN)))
    for obj in objs :
        if obj['name'] == username :
            if obj['name'] == username and obj['password'] == password :
                print(f"Welcome {obj['name']},")
                if obj['admin'] :
                    print(f"Here is your flag: {FLAG}")
                print("Goodbye, See you again.")
            else :
                print("Failed to login.")
except :
    print("Token not authorized")
