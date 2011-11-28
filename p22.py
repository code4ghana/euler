from urllib2 import urlopen



data=urlopen("http://projecteuler.net/project/names.txt").readlines()
mylist=data[0].replace("\"","").rsplit(",")
mylist.sort()
sums=0
for i,e in enumerate(mylist):
        alphaValue=sum([ord(v.lower())-96 for v in e])
        sums+= alphaValue*(i+1)
       
print sums
