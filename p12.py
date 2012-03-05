divisors={1:[1],2:[1,2],3:[1,3]}
def finddivs(num,found=set()):
    divs=set([num,1])
    #-------------
    for i in range(int(num/2)+1,2,-1):
        if num%i is 0:
            if i not in found:
                if i in divisors:
                    divs.add(i)
                    found.add(i)
                else:
                    finddivs(i,found)
                continue
    divisors[num]=list(divs)
    return divs
            
                

def triangleNumberGenerator():
    n=2;
    while True:
        yield int((n*n+n)/2)
        n+=1


if __name__== "__main__":
    print finddivs(20)
    print divisors
