import sys

def mysum(fileName):
    with open(fileName,"r") as f:
        tot=0
        for i in f:
            tot+=long(i)
        print tot



if len(sys.argv) is 1:
    print "please supply matrix file name"
    exit
mysum(sys.argv[1])
