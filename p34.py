cache={0:1,1:1,2:2,3:6,4:24,5:120,6:720,7:5040,8:40320,9:362880}
tot=0

for i in xrange(3,10000):
    if sum(map(cache.get,map(int,str(i)))) is i:
        print i
        tot+=i
print tot
