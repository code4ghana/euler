from math import sqrt,ceil



def primes_upto(top):
    myList=[2]
    myList[1:]=xrange(3,top,2)
    stopOn=int(sqrt(top))+1
    stopPos=int(ceil(stopOn/2))
    for i in myList[1:stopPos]:
        if i >0:
            for inner in xrange(i*i,top,i):
                if inner & (1):
                    num=int(ceil(inner/2))
                    if myList[num]:
                        myList[num]=0;
    return myList

if __name__=="__main__":
    import sys
    
    if len(sys.argv)<3:
        print "--input--> [(s)um|(h)ighest] [non-zero integer]  <---output prime info"
        exit()
    if sys.argv[1] is "sum" or (sys.argv[1])[0] is "s":
        print "The sum of primes under",sys.argv[2],"is",sum(primes_upto(int(sys.argv[2])))
        exit()
    if sys.argv[1] is "highest" or (sys.argv[1])[0] is "h":
        primes=primes_upto(int(sys.argv[2]))
        nonzeros=[i for i in primes if i]
        print "The highest prime under ",sys.argv[2]," is ",[i for i in primes if i][-1]
