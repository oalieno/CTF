import string

good = string.ascii_letters + string.punctuation + string.digits + ' '

encrypt = "809fdd88dafa96e3ee60c8f179f2d88990ef4fe3e252ccf462deae51872673dcd34cc9f55380cb86951b8be3d8429839".decode('hex')

message = "flag{"
key = "*3|!o"

def to_binary(x):
    ans = ""
    for word in x: ans += "{:08b}".format(ord(word))
    return ans

def find_possible(n,key):
    for i in xrange(0,len(encrypt)-len(key)+1):
        encrypt_binary = to_binary(encrypt[i:i+len(key)])
        key_binary = to_binary(key)
        message_binary = ""
        for j in xrange(0,len(key)*8,n):
            mask = (1 << n) - 1
            now = ((mask + 1) + int(encrypt_binary[j:j+n],2) - int(key_binary[j:j+n],2)) & mask
            message_binary += ("{:0" + str(n) + "b}").format(now)
        ans = ""
        try:
            for j in xrange(0,len(message_binary)-8+1,8):
                ch = chr(int(message_binary[j:j+8],2))
                if ch not in good: raise Exception
                ans += ch
        except: continue
        print "i:",i
        print "message:",ans

for n in xrange(1,8):
    print "n:",n
    find_possible(n,"flag{")

find_possible(5,"mZ440")

'''
n = 5

for i in xrange(0,len(encrypt)-n+1,n):
    print "i:",i
    for _1 in good:
        for _2 in good:
            for _3 in good:
                for _4 in good:
                    for _5 in good:
                        try:
                            encrypt_binary = to_binary(encrypt[i:i+n])
                            binary = to_binary(_1+_2+_3+_4+_5)
                            message_binary = ""
                            for j in xrange(0,len(binary)-n+1,n):
                                mask = (1 << n) - 1
                                now = ((mask + 1) + int(encrypt_binary[j:j+n],2) - int(guess_binary[j:j+n],2)) & mask
                                message_binary += ("{:0" + str(n) + "b}").format(now)
                            message = ""
                            for j in xrange(0,len(message_binary)-8+1,8):
                                ch = chr(int(message_binary[j:j+8],2))
                                if ch not in good: raise Exception
                                message += ch
                            print "i",i
                            print message
                            print _1+_2+_3+_4+_5
                        except:
                            continue
'''

'''    
for n in xrange(2,3):
    for i in xrange(len(encrypt)):
        possible = []
        for guess in good:
            encrypt_binary = to_binary(encrypt[i])
            guess_binary = to_binary(guess)
            message_binary = ""
            for j in xrange(0,8,n):
                mask = (1 << n) - 1
                now = ((mask + 1) + int(encrypt_binary[j:j+n],2) - int(guess_binary[j:j+n],2)) & mask
                message_binary += ("{:0" + str(n) + "b}").format(now)
            if chr(int(message_binary,2)) not in good: continue
            possible.append(chr(int(message_binary,2)))
        if len(possible) == 0: break
        print "i:",i
        print ''.join(possible)
'''        

'''
for n in xrange(1,8):
    encrypt_binary = to_binary(encrypt)
    message_binary = to_binary(message)
    key_binary = ""
    #print encrypt_binary
    #print message_binary

    for i in xrange(0,len(message_binary),n):
        if i+n > len(message_binary): break
        mask = (1 << n) - 1
        now = ((mask + 1) + int(encrypt_binary[i:i+n],2) - int(message_binary[i:i+n],2)) & mask
        key_binary += ("{:0" + str(n) + "b}").format(now)

    ans = ""

    try:
        for i in xrange(0,len(key_binary),8):
            if i+8 > len(key_binary): break
            ch = chr(int(key_binary[i:i+8],2))
            if ch not in good: raise Exception
            ans += ch
    except: continue

    print "n:",n
    print "len:",len(ans)
    print "key:",ans
'''
