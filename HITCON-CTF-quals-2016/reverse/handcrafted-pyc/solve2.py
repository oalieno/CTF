with open("disassembly-code") as data:
    code = data.read()

ans = ""

for line in code.strip().split('\n'):
    if "LOAD_CONST" in line:
        num = line.split('(')[1].split(')')[0]
        if num == 'None': continue
        ans += chr(int(num))

print ans
