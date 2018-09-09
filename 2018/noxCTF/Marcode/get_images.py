#!/usr/bin/env python3
import os
import requests
import threading
from pyzbar.pyzbar import decode
from PIL import Image

class myThread (threading.Thread):
    def __init__(self, filenames):
        threading.Thread.__init__(self)
        self.filenames = filenames
        self.downloadURL = "https://drive.google.com/uc?authuser=0&id={}&export=download"

    def get_image(self, filename):
        i = filename.strip('frame').strip('.jpg')
        data = decode(Image.open('keyframes/{}'.format(filename)))[0].data.decode()
        gdrive_id = data.split('=')[1]
        r = requests.get(self.downloadURL.format(gdrive_id))
        with open('pictures/{}.png'.format(i), 'wb') as f:
            f.write(r.content)
    
    def run(self):
        for filename in self.filenames:
            self.get_image(filename)


filenames = os.listdir('keyframes')
threads = []

for i in range(0, len(filenames), 50):
    thread = myThread(filenames[i:i+50])
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

print('done')
