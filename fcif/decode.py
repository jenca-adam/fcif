from .bytes2int import *
from .misc import *
from .version import __version__ 
#from .pallete import pallete
from .percentage import percy
import gzip
import io
from PIL import Image
class VersionMismatch(Exception):pass
def throw():
    raise ValueError("file does not match specifications.")

def decode(stream):
    
    bts=open(stream,'rb')
    bts.seek(0)
    print('decoding...')
    print('reading header...')
    if bts.read(1)!=b'\xaa':throw()
    if bts.read(4)!=b'FCIF':throw()
    vrs=b''
    while True:
        ff=bts.read(1)
        if ff==b'\xde':
            break
        vrs+=ff
    vers='.'.join([str(com) for com in vrs])
    print(f'image version {vers}')
    if vers != __version__:
        raise VersionMismatch(f"FCIF versions {vers} and {__version__} do not match!")
    print('reading pallete...')
    lpall=bytes2int(bts.read(1))
    mxa=(i for i in bts.read(3))
    lpalb=bytes2int(bts.read(1))

    plt=decode_tups(bts.read(lpalb),mxa,lpall)
    print(plt)
    plt_rgb=plt
    bts.read(2)
    print('reading size...')
    width_blength=bytes2int(bts.read(1))
    height_blength=bytes2int(bts.read(1))
    width=bytes2int(bts.read(width_blength))
    height=bytes2int(bts.read(height_blength))
    print(bts.read(2))
    print(f'size: {width}x{height}')
    maxpalbits=(len(plt)-1).bit_length()
    print('reading byte flow...')
    mxrwl=bytes2int(bts.read(1))
    mxrw=bytes2int(bts.read(mxrwl))
    tpll = bytes2int(bts.read(1))
    tpl = bytes2int(bts.read(tpll))
    mxlec=bytes2int(bts.read(1))

    btf=gzip.decompress(bts.read())
    print(len(btf))
    print(mxlec,mxrw,tpl)
    coll=decode_tups(btf,(mxlec,mxrw),tpl)
    it=iter(coll)
   
    curll=0
    curlc=next(it)
    print(curlc)
    im=Image.new("RGB",(width,height),plt[curlc[0]])
    pix=im.load()
    for y in range(height):
        for x in range(width):
            if curll==curlc[-1] or curlc[-1]==0:
                curll=0
                try:
                    curlc=next(it)
                except StopIteration:
                    print('w')
                    return im
            curll+=1
            try:
                pix[x,y]=plt[curlc[0]]
            except:
                raise
                return im
    return im


    
    
    
