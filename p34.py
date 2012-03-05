cache={0:1,1:1,2:2,3:6,4:24,5:120,6:720,7:5040,8:40320,9:362880}
tot=0

for i in xrange(10,2540160):
    vals=[int(j) for j in str(i)]
    facts=[cache[j] for j in vals]
    together=sum(facts)
    if together==i:
        print together
        tot+=together
    
print "total is ",tot
