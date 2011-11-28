import sys,os,operator,csv

def importMatrix(fileName,separator):
    with open(fileName,"r") as f:
        for line in csv.reader(f,delimiter=separator,skipinitialspace=True):
            if line:
                yield line

def rowOrColumnMax(matrix, winSize):
    win=[]
    value=0
    for row in matrix:
#        print row
        if len(row)<winSize:
            return
        for i in xrange(0,len(row)-(winSize-1)):
            curWin=[int(x) for x in row[i:i+winSize]]
            curValue=reduce(operator.mul,curWin,1)
            #print "window is: ",win,"value is:",curValue
            if value<curValue:
               # print "new max window",win,"new value is",curValue
                value=curValue if value<curValue else value
                win=curWin
    return win,value

def diagToRows(matrix):
    maxRowLength=min(len(matrix),len(matrix[0]))
    blankMatrix=[]
    for i in xrange(1,maxRowLength):
        blankMatrix.append([0]*i)
    for i in xrange(maxRowLength-1,1,-1):
        blankMatrix.append([0]*i)
    return blankMatrix

def leftDiagWalk(matrix,length=None,width=None):
    length= length if length else len(matrix)-1
    width=width if width else len(matrix[0])-1
    x,y=0,0
    for dummy in xrange(length*width):
#        print matrix[x][y]
        yield matrix[x][y]
        if x is 0 and y is length:
            print "hit corner going to ", matrix[x][y]
            x=length
            y=1
        elif x is 0:
            print "hit ceiling ", matrix[x][y]
            x=y+1
            y=0
        elif y is width:
            print "hit right wall",matrix[x][y]
            y=x+1
            x=length
     
        else:
            x-=1
            y+=1

        

    
def fillMatrix(oldMatrix,matrix):
    gen=leftDiagWalk(oldMatrix)
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j]=gen.next()
    return matrix


if len(sys.argv) is 1:
    print "please supply matrix file name"
    exit
matrix=[x for x in importMatrix(sys.argv[1]," ")]
rowMax=rowOrColumnMax(matrix,4)
print "max in ROWS:",rowMax
columnMax=rowOrColumnMax(zip(*(matrix[:])),4)
print "max in COLUMNS:",columnMax
#for row in matrix:
 #   print row
print "column transposed matrix"
blankMatrix=diagToRows(matrix)
for row in fillMatrix(matrix,blankMatrix):
    print row

print "the matrix at 0,1 is ",matrix[0][1]
