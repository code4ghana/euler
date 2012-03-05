from p18 import TreeNode, importMatrix, findtarg

def createTree(int_matrix):
	matrix=[]
	
	heuristics={len(int_matrix[-1])+1:0,len(int_matrix[-1]):max(int_matrix[-1])}
	matrix.append([TreeNode(level=len(int_matrix[-1]),  children=[], heu=0, val=n) for n in int_matrix[-1]])
	for row in reversed(int_matrix[:-1]):
		nodeRow=[]
		best=0
		#print [str(i)+' '+str(e.val) for i,e in enumerate(matrix[-1])]
		print '------------------'
		#print matrix[-1][0]
		#print row

		for ind,num in enumerate(row):

                   # if (ind>0 and ind<len(row)-1) and (num < row[ind-1] and num< row[ind+1]):
                    #    nodeRow.append(None)
                       # print "pruned node ", num
                     #   continue
                    

                    c1=matrix[-1][ind]
                    c2=matrix[-1][ind+1]
                    node=TreeNode(heu=heuristics[len(row)+1], children=[c1,c2], val=num, level=len(row))
                    #print node, '-->',
                    if c1:
                        c1.updateParent(node)

                    if c2:
                        c2.updateParent(node)
                    nodeRow.append(node)
                   # print c1.val if c1 else "pruned",
                   # print c2.val if c2 else "pruned"
                    
                    best= num if num > best else best
                matrix.append(nodeRow)
		heuristics[len(row)]=best+heuristics[len(row)+1]
  
        vals=[n.getTot() for n in matrix[0] if n]
	return matrix[-1][0],vals

if __name__=='__main__':


    import sys
    if len(sys.argv) is 1:
        print "please supply matrix file name"
        exit()

        
    table = [[int(n) for n in s.split()] for s in open(sys.argv[1]).readlines()]
    
    for row in range(len(table)-1, 0, -1):
        for col in range(0, row):
            table[row-1][col] += max(table[row][col], table[row][col+1])
    print "Answer to PE18 = ", table[0][0]
    
    #int_matrix=[list([int(i) for i in x]) for x in importMatrix(sys.argv[1]," ")]
    #ret=createTree(int_matrix)
    #print ret[0],ret[1]
