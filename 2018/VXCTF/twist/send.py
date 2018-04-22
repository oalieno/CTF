#!/usr/bin/env python3
import time
import json
import requests
import itertools

headers = {
    "user-agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
    "cookie" : "__cfduid=d9e31b4f0ef435d298229bf79abf101811521191558; _ga=GA1.2.913974771.1521191559; _gid=GA1.2.1145344492.1524290237; userToken=997d48c2e736bfbc6fd3acdb418659d28cab01621ac993c475ceba203760947632a0f34b7fd9eed4ad5aebd868937297f7a57e6d4a950d5bac81e62ca340924acb31739d430375341712f1f6e7bedffc5bc17e7e9991a3e47458d0b627f3e21b5d28077177ee2cf177c0293857b210237f507d4fa8a319ef18592eefdde4d091"        
}

possible = ['{', 'rR', 'nN', 'tT', 'cC', 'rR', 'eE3', 'aA4', 'wW', '}']

flag = "vxctf{}A{}3_u_d01{}5_1{}_bY_f0r{}3_o{}_TH{}_sM{}rT_{}4Y?{}".format(*list(itertools.product(*possible))[34])

for guess in itertools.product(*possible):
    data = {
        #"flag" : "vxctf{}A{}3_u_d01{}5_1{}_bY_f0r{}3_o{}_TH{}_sM{}rT_{}4Y?{}".format(*(guess))
        "flag" : flag
    }
    r = requests.post("https://ctf.vxcon.hk/api/challenges/flag/35", headers = headers, data = data)
    result = json.loads(r.text)
    print(result["info"]["correct"], result["info"]["message"])
    time.sleep(0.5)
