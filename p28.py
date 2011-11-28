import sys

def spiralCount(dim):
    top=dim*dim
    tot=1
    prev=1
    incr=2
    while prev <top:
        tot+=4*prev+10*incr
        prev=prev+4*incr
        incr+=2
    return tot

if len(sys.argv)<2:
    print "type the length of the side of the square ex:4"
    exit()
found=spiralCount(int(sys.argv[1]))
print "sum of the diagonals around the spiraly square is ",found
