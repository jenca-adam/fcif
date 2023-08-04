import math
def int2bytes(i):
    return int(i).to_bytes(blength(i),'big')
def bytes2int(b):
    return int.from_bytes(b,'big')
def blength(n):
    n=int(n)
    bl=n.bit_length()
    if bl==0:
        bl=1
    return math.ceil(bl/8)

