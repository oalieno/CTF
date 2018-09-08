#!/usr/bin/env python3
from base64 import *

start = 0x3e971

data = open('./snake.jpg', 'rb').read()
open('file.zip', 'wb').write(b64decode(data[start:].replace(b'\r\n', b'').strip()))
