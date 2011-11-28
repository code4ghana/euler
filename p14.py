
def collatz(top):
    cache={1:1,2:1}

    top=top if top&(1) else top-1
    maxChain=1
    num=1
    for n in xrange(1,top+1,2):
#        print "n: ",n
        curChain=0
        next=n
        while next not in cache:
 #           print next," not in cache"
            curChain+=1
            next=3*next+1 if next&(1) else next/2
            
# o       print "cache says",next,"=",cache[next]
        curChain+=cache[next]
        cache[n]=curChain
#        print "cache updated",n," points to ",cache[n]
        if curChain>maxChain:
            maxChain=curChain
            num=n
#    print cache
    return maxChain ,num

print collatz(1000000)
