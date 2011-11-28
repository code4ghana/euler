def testComb(items,r):
    pool=tuple(items)
    n=len(pool)
    if r>n:
        return
    indices=range(r)
    yield tuple(items[i] for i in indices)
    while True:

        for i in reversed(range(r)):
            if indices[i] !=i+n-r:
                break
        else:
            return
        indices[i]+=1
        
        for j in range(i+1,r):
            indices[j]=indices[j-1]+1
        yield tuple(pool[i] for i in indices)

if __name__=="__main__":
    import itertools
    mil=999999
    for index,element in enumerate(itertools.permutations("0123456789",10)):
            print element


