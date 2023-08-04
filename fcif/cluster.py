from sklearn.cluster import MiniBatchKMeans as KMeans
from numpy import int16,array
from .misc import rmsim
def mkpa(l,MCP):
    print("p",l)
    if l>MCP:
        return MCP
    return l
def arr2tup(arr):
    return tuple(map(tuple,arr))
def makePoints(clr):

    pts = []
    for l,cl in clr:
        pts.extend(l*[cl])
    return pts
def _kmeans(points,n):
    print("cc",n)
    j=KMeans(n_clusters=n)
    j.fit(points)
    return list(set(arr2tup(int16(j.cluster_centers_))))
def Cluster(points,MCP):
    print("mcp",MCP)
    if len(points)<=MCP:
        return [i[0] for i in points]
    x=points
    return sorted(_kmeans(x,mkpa(
        len(set(points)),MCP
        )))
