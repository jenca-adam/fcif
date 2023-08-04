from .encode import *
from .decode import *
import os
import click
@click.command()
@click.argument("fn")
@click.option("--palette",default=20,help="Palette size")
def main(fn,palette):
    """FCIF(few colors image format) is a lossy image compression alghoritm, mostly focused on graphics that don't use many colors(like icons or simple logos). It uses a combination of reducing color palette using K-means clustering and run-length encoding of color sequences to provide up to 30% the size for certain images"""
    try:
        by=convert(fn,palette)
    except KeyboardInterrupt:
        raise
    except:
        a=decode(fn)
        print(a)
        a.show()
        return
    origs=os.stat(fn).st_size
    news=len(by)
    print(f'Original size:{origs}. New size:{news}({round((news/origs)*100,2)}%)')
    nfn=os.path.splitext(fn)[0]+'.fcif'
    print(f'Saving as {nfn!r}')
    open(nfn,'wb').write(by)
main()
