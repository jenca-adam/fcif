from . import pallete

from . import version
from . import bytes2int
from . import percentage
from .misc import *
from .pngopener import openim
import dill
import gzip
import pickle
def convert(image,MCP=20):
    print('Converting...')
    print('Making header')
    print('Getting version data..')
    vrs=b''.join([bytes2int.int2bytes(int(i)) for i in version.__version__.split('.')])
    r=b'\xaaFCIF'+vrs+b'\xde'
    im=openim(image)
    im = im.convert("RGB")#!!!!
    print('Getting pallete...')
    pal=pallete.pallete_from_img(im,MCP)
    print(pal.plt)
    pltbs=bytearray()
    print('Writing pallete...')
    pltbs.append(len(pal))
    pltbs.extend(gmax(pal))
    j=encode_tups(pal.plt)
    print(len(j))
    pltbs.append(len(j))
    pltbs.extend(j)
    r+=pltbs
    print('Writing size...')
    r+=b'\xde\xda'
    r+=bytes2int.int2bytes(bytes2int.blength(im.width))
    r+=bytes2int.int2bytes(bytes2int.blength(im.height))
    r+=bytes2int.int2bytes(im.width)
    r+=bytes2int.int2bytes(im.height)
    r+=b'\xda\xff'
    print('Header made')

    maxpalbits=(len(pal)-1).bit_length()
    maxlenlen=2**(2*(8-maxpalbits)-1)
    print('Encoding image...')
    pix=im.load()
    colors=[]
    lc=-1
    lcl=0
    maxlcl=0
    
    for y in range(im.height):
        for x in range(im.width):
            color=pal.closest(pix[x,y])
            if color==lc:
                lcl+=1
            
            else:
                if lc>=0:
                    maxlcl=max(maxlcl,lcl)
                    colors.append((lc,lcl))
                lc=color
                lcl=1
    colors.append((lc,lcl))
    gm=[len(set(dict(colors).keys())),maxlcl]
    print(gm,len(colors),im.width*im.height)

    colorsn=encode_tups(colors,gm)
    r+=bytes2int.int2bytes(bytes2int.blength(maxlcl))
    
    r+=bytes2int.int2bytes(maxlcl)
    r+=bytes2int.int2bytes(bytes2int.blength(len(colors)))
    r+=bytes2int.int2bytes(len(colors))


    r+=bytes2int.int2bytes(gm[0])

    print(len(colorsn))
    print(len(gzip.compress(colorsn)))
    r+=gzip.compress(colorsn)
    return r


