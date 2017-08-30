def b9(x):
    return "{:09b}".format(x)

def b18(x):
    x = "{:018b}".format(x)
    return x[9:18] + x[:9]

def b27(x):
    x = "{:027b}".format(x)
    return x[9:18] + x[:9] + x[18:27]

def b54(x):
    return b27(x >> 27) + b27(x & 0x7FFFFFF)
