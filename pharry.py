import re

def permute(v,start,n):
    if start == n-1:
        for i in v:
            print i,
    else:
        for i in range(start,n):
            tmp = v[i]
            v[i] = v[start]
            v[start] = tmp
            permute(v, start+1, n)
            v[start] = v[i]
            v[i] = tmp


def partition(num):
    combs=[num]
    for i in range(num-1,0,-1):
        goten=partition(num-(num-i))
        for j in goten:
            combs.append([num-i,j])
    return combs

def weights(maxweights,weights):
    validParts=[]
    for i in partition(maxweights):
        vals=re.sub(r'[\[\] $]*',"",str(i))
        if len(vals.split(",")) is weights:
            anonList=vals.split(",")
            print anonList
            permute(anonList,0,len(anonList))            
    return validParts


if __name__=="__main__":
    import sys
    
    if len(sys.argv)<3:
        print "--input--> [integer: weight sum] [integer: number of weights] <---possible weights"
        exit()
    for i in weights(int(sys.argv[1]),int(sys.argv[2])):
        print i
        

