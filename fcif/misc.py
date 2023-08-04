import itertools
import math
import numpy as np
try:
    from .percentage import percy
except:
    from percentage import percy
def getbytes(bits):
    bits=iter(bits)
    done = False
    while not done:
        byte = 0
        for _ in range(0, 8):
            try:
                bit = next(bits)
            except StopIteration:
                bit = 0
                done = True
            byte = (byte << 1) | bit
        yield byte
def rmsim(x):
    b=[]
    j=None
    for i in x:
        if j is not None:
            if euclidean(i,j)>0.1:
                b.append(i)
        j=i
    return b
def mint(r,g,b):
    r,g,b = r//2,g//2,b//2
    return r*128**2 + g*128+b
def mrgb(i):
    b,g,r = i%128,i//128%128,i//128//128
    return r*2,g*2,b*2
def _bin(num):
    binary = []
    while num > 0:
        bit = num % 2
        binary.append(bit)
        num //= 2
    binary.reverse()
    return binary
def getc(cl):
    if not isinstance(cl,tuple):
        return (cl,)*3
    elif len(cl)>3:
        return cl[:3]
    return cl
def gbl(i):
    i=int(i)
    if i==0:
        return 1
    return i.bit_length()
def bitfield(n,width=None):
    n=int(n)
    bt=_bin(n)
    if width is None or width<n.bit_length():return bt
    return [0]*(width-n.bit_length())+bt
def gln(m,l):
    x=l*m.bit_length()
    return math.ceil(x/8)
def closest(cls,cl):
    colors = np.array(cls)
    color = np.array(getc(cl))
    distances = np.sqrt(np.sum((colors-color)**2,axis=1))
    index_of_smallest = np.where(distances==np.amin(distances))
    return index_of_smallest[0][0]
def _range(a,b,c):
    if c==0:
        return []
    return range(a,b,c)
def grouper(n,input):
    a= [input[i:i+n] for i in _range(0, len(input), n)]
    return a
def encode_nums(nums):
    print('Running bit compression...')
    maxbits=len(bitfield(max(nums)))
    bits=[]
    for num in percy(nums):
        bits.extend(bitfield(num,maxbits))
    return bytes(getbytes(bits))
    #return bits
def decode_nums(bts,mxa,l):
    print('Running bit decompression...')
    mx=len(bitfield(mxa))    
    l*=mx
    
    bits=[]
    for bt in percy(bts):
        bits.extend(bitfield(bt,8))
        #bits.extend(bt)
    bits=bits[:l]
    bits=grouper(mx,bits)
    nums=[ int(''.join([str(a) for a in i]),2)for i in bits]
    return nums
def gmax(tups):
    x=[-1]*len(tups[0])
    for i in tups:
        for a,b in enumerate(i):
            if x[a]<b:
                x[a]=b
    return x
def encode_tups(tups,x=None):
    if x is None:
        x=gmax(tups)
    maxbits=tuple([gbl(i) for i in x])
    bitf=[]
    for tup in tups:
        for ix,it in enumerate(tup):
            
            bitf.extend(bitfield(it,maxbits[ix]))
    return bytes(getbytes(bitf))
def decode_tups(bts,mxs,ln):
    print(mxs)
    mxss=tuple(gbl(i) for i in mxs)
    bits=[]
    for bt in bts:
        bits.extend(bitfield(bt,8))

    bits=bits[:(ln*sum(mxss))]
    bits=grouper(sum(mxss),bits)
    tups=[]
    for bit in bits:
        tup=[]
        for mx in mxss:
            if  not bit:break
            frog=bit[:mx]
            tup.append(int(''.join([str(a) for a in frog]),2))
            bit=bit[mx:]            
        tups.append(tuple(tup))
    return tups
def tee(it):
   return itertools.tee(it)[0]
def baseround(tup,base):
    ntu=[]
    for num in tup:
        mod=num%base
        if mod<=num//2:
            ntu.append( num-mod)
        else:
            ntu.append(num+(base-mod))
    return tuple(ntu)
def euclidean(vect1,vect2):
    return math.sqrt(sum((el-vect2[ex])**2 for ex,el in enumerate(vect1)))
class getiter:
    def __init__(self,it):
        self.it=tee(iter(it))
    def __getitem__(self,ix):
        _tempit=tee(self.it)
        for _ in range(ix+1):
            try:
                a=next(_tempit)
            except StopIteration:
                raise IndexError
        return a
    def __iter__(self):
        return tee(self.it)
