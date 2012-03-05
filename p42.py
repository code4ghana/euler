
if __name__=="__main__":

    from urllib2 import urlopen
    nthTriangle=lambda n:int((n*n+n)/2)
    triangles=set([nthTriangle(i) for i in range(1,30)])
    loc="http://projecteuler.net/project/words.txt"
    data=urlopen(loc).readlines()
    mylist=data[0].replace("\"","").rsplit(",")
    mylist.sort()
    vals=0
    for word in mylist:
        alphaValue=sum([ord(v.lower())-96 for v in word])
        if alphaValue in triangles:
            vals+=1
        
        print word,"=",alphaValue,"--->",alphaValue in triangles 
    print "triangles --",triangles
    print vals
