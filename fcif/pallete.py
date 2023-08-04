import itertools
import operator
from scipy.spatial import distance
from .cluster import Cluster
from .misc import baseround,getc,closest
from . import percentage
from PIL import Image
import numpy as np
from .misc import mint,mrgb,rmsim
def pallete_from_img(im,MCP):
    print("pmcp",MCP)
    plt=im.getdata()
    clu=Cluster(plt,MCP)
    print("pal len",len(clu))
    return Pallete(clu)
class Pallete:
    def __init__(self,pltl):
        print(pltl)
        self.plt=np.array(pltl)
        self._cc={}
    def __iter__(self):
        return iter(self.plt)
    def closest(self,col):
        if col in self._cc:
            return self._cc[col]

        j=closest(self.plt,col)
        self._cc[col]=j
        return j
    def index(self,item):
        for index,it in enumerate(self.plt):
            if it==item:
                return index
        raise IndexError
    def __len__(self):
        return len(self.plt)
    def __getitem__(self,i):
        return self.plt[i]

