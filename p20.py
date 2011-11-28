num=1
for i in xrange(1,100):
    num=num*i

nums=[i for i in str(num)]
sum=0
for i in nums:
    sum+=int(i)
print sum


