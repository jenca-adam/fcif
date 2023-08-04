def percy(l):
    ll=len(l)
    for ix,it in enumerate(l):
        print(f'{round((ix/ll)*100)}% done',end='\r')
        yield it
    print()
    

