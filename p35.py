cache=set([])
rotary={}
def rotate(broken):
    length=len(broken)
    concat=broken*2

    for i in range(length):
        conf=int("".join(concat[i:i+length]))
        yield conf

def isRotary(num):
    broken=[i for i in str(num)]
    joined=int("".join(broken))
    if num not in cache:
        return False
    for i in broken:
        if not int(i)&(1):
            return False
    if joined in rotary:
        return rotary[int("".join(broken))]
    
    for i in rotate(broken):
        if i not in cache:
            rotary[joined]=False
            return False
    rotary[joined]=True
    return True
def rotaries(top):
    for i in cache:
        if isRotary(i):
            yield i

if __name__=="__main__":
    import sys
    from p10 import primes_upto
    if len(sys.argv)<3:
        print "--input--> [(r)otary|(c)heck] [non-zero integer]  <---output rotary prime info"
        exit()


    if sys.argv[1] is "rotary" or (sys.argv[1])[0] is "r":
        cache.update([i for i in primes_upto(int(sys.argv[2])) if i])
        print "The rotary primes under %i  are",int(sys.argv[2])
        rots=1
        for i in rotaries(int(sys.argv[2])):
#            print i
            rots+=1
        print "There are %i circular numbers" % rots
        exit()
    if sys.argv[1] is "check" or (sys.argv[1])[0] is "c":
        cache.update([i for i in primes_upto(int(sys.argv[2])+1) if i])
        print sys.argv[2],"is",isRotary(int(sys.argv[2]))

