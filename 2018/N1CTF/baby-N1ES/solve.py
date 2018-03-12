#!/usr/bin/env python
from N1ES import N1ES
import base64
key = "wxy191iss00000000000cute"
n1es = N1ES(key)
cipher = "HRlgC2ReHW1/WRk2DikfNBo1dl1XZBJrRR9qECMNOjNHDktBJSxcI1hZIz07YjVx"
cipher = base64.b64decode(cipher)
print n1es.decrypt(cipher)
