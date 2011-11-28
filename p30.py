import sys

def sameSum(power):
    cache=dict((x,x**power) for x in xrange(0,10))
    found=[]
    for num in xrange(2,2000000):
        val=sum([cache[int(j)] for j in str(num)])
        if val ==  num:
            found.append(num)
    return found

if len(sys.argv)<2:
    print "type the power"
    exit()
found=sameSum(int(sys.argv[1]))
print found
print "sum",sum(found)
