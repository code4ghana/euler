import sys

def fibDigits(digits):
    prev=1
    prev2=1
    fib=2
    curLength=1
    while curLength<digits:
        prev,prev2=prev2,prev+prev2
        fib+=1
#        print "prev ",prev,"prev2 ",prev2
        curLength=len(str(prev2))
    print "Fib of ",fib," has ",curLength,"digits and is ",prev2
#    print prev2
    
if len(sys.argv)<2:
    print "--input--> [(s)um|(h)ighest] [non-zero integer]  <---output prime info"
    exit
fibDigits(int(sys.argv[1]))
        
