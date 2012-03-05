#We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.
#What is the largest n-digit pandigital prime that exists?
cache=[]
def highPandigital():
    best=0
    num=0
    for i in cache:
        size=len(str(i))
        for j in range(1,size+1):
            if str(j) not in list(str(i)):
                break
        else:
            best=len(str(i)) if len(str(i))>=best else best
            num=i
    return best,num

            
            
if __name__=="__main__":
    import sys
    from p10 import primes_upto
    if len(sys.argv)<2:
        print "--input--> [(h)ighest] [non-zero integer]  <---output pandigital information"
        exit()
    
    cache.extend([i for i in primes_upto(int(sys.argv[1])) if i])
    print "The highest pandigital number is ",highPandigital()
