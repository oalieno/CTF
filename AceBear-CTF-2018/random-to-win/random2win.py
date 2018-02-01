import os
import socket
import threading
from hashlib import *
import SocketServer
import random
from Secret import flag, p, h
host, port = '0.0.0.0', 33337
BUFF_SIZE = 1024
assert len(str(p)) == 121

class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    allow_reuse_address = True

class ThreadedTCPRequestHandler(SocketServer.BaseRequestHandler):
    def test(self):
        r = random.randint(0,222222)
        i = 2
        while i>0:
            self.request.sendall("Message: ")
            m = self.request.recv(BUFF_SIZE).strip()
            m = int(m.encode('hex'),16)            
            c = (r*h+m)%p
            self.request.sendall("Ciphertext: %s\n" %c)
            i -=1
        
        
    def submit(self):
        m = random.randint(10**10,10**12)
        r = random.randint(10**10,10**12)
        c = (r*h+m)%p
        print m, r
        self.request.sendall("Ciphertext: %s\n" %c)
        x = self.request.recv(BUFF_SIZE).strip()
        if(m == int(x)):
            self.request.sendall(flag)

    def view(self):
        while True:
            self.request.sendall("********************Menu********************\n")
            self.request.sendall("* 1 - Test                                 *\n")
            self.request.sendall("* 2 - Submit                               *\n")
            self.request.sendall("********************************************\n")
            self.request.sendall("Your choice: ")
            try:
                choice = int(self.request.recv(BUFF_SIZE).strip())
            except:
                choice = 0
            if choice == 1:
                self.test()
                break
            elif choice == 2:
                self.submit()
                break
            else:
                self.request.sendall("Invalid choice!\n")
	   
    def handle(self):
        self.request.settimeout(10)        
        self.view()
    

def main():
	server = ThreadedTCPServer((host, port), ThreadedTCPRequestHandler)
	server_thread = threading.Thread(target=server.serve_forever)
	server_thread.daemon = True
	server_thread.start()
	print "Server loop running in thread:", server_thread.name
	server_thread.join()

if __name__=='__main__':
    main()

