import csv,random
class TreeNode():
        def __init__(self,level,heu,val,children=[]):
		self.level=level
		self.h=heu+val
		self.children=[child for child in children if child]
		self.val=val
		self.g=0
		self.f=self.g+self.h
		self.parent=None
		self.UID=random.random()
		self.depth=0
		self.tot=None
		
        def updateParent(self,p):
		if self.parent== None or self.parent<=p :
			self.depth=p.getDepth()+1
			self.parent=p
			self.updateGScore()
			

        def __repr__(self):
		return "level: %(level)i, value: %(value)i h: %(h)i, f: %(f)i ID: %(ID)f |" % {'level':self.level,'value': self.val,'h': self.h,'f': self.f,'ID':self.UID}

        def __eq__(self,other):
		if other is None:
			return False
		return self.UID is other.UID

        def __lt__(self, other):
		return self.f < other.f
        
        def updateGScore(self):
		self.g=self.parent.g+self.parent.val
		self.f=self.g+self.h

	def traceback(self):
		path=[self]
		parent=self.parent
		while parent:
			path.append(parent)
			parent=parent.parent
		return reversed(path)    
	def getDepth(self):
		return self.depth

	def getChildren(self):
		return self.children

	def getTot(self):
		if not self.tot:
			self.tot=self.val if self.parent is None else self.val+self.parent.getTot()
		return self.tot
	
def importMatrix(fileName,separator):
	with open(fileName,"r") as f:
		for line in csv.reader(f,delimiter=separator,skipinitialspace=True):
			if line:
				yield line




def findtarg(first,depth=0):
        openList=[first]
	print first, depth
	print ' ,'.join([str(child.val) for child in first.getChildren()])
	for child in first.getChildren():
		if child:
			child.updateParent(first)
			openList.append(child)
		
        print [i for i in openList]
	closedList=[first]
	openList.remove(first)


        print "closed ",[i for i in closedList]
	print "open",[i for i in openList]
	while(len(openList)):
		best=max(openList)
		print 'at: ',best
		if best.getDepth() == depth:
			return best.traceback(),len(openList)+len(closedList)
		closedList.append(best)
		openList.remove(best)
		adjacents=best.getChildren()
		changed=False
		for i in adjacents:

			if i in closedList:
				continue
			loc=None
			i.updateParent(best)
			if i not in openList:
				openList.append(i)
				changed=True
				new_better=True
				loc=len(openList)-1
			elif i.g < openList[openList.index(i)].g:
				new_better=True
				loc=openList.index(i)
			
			else:
				new_better=False
			if new_better:
				openList[loc].updateParent(best)
				changed=True
		if changed:
			openList.sort()

	return None






def createTree(int_matrix):
	matrix=[]
	
	heuristics={len(int_matrix[-1])+1:0,len(int_matrix[-1]):max(int_matrix[-1])}
	matrix.append([TreeNode(level=len(int_matrix[-1]), children=[], heu=0, val=n) for n in int_matrix[-1]])
	for row in reversed(int_matrix[:-1]):
		nodeRow=[]
		best=0
		#print [str(i)+' '+str(e.val) for i,e in enumerate(matrix[-1])]
		print '------------------'
		#print matrix[-1][0]
		#print row

		for ind,num in enumerate(row):
			c1=matrix[-1][ind]
			c2=matrix[-1][ind+1]
			
			node=TreeNode(heu=heuristics[len(row)+1], children=[c1,c2], val=num, level=len(row))
			print node,'--> ',c1.val,c2.val
			nodeRow.append(node)
			best= num if num > best else best
		matrix.append(nodeRow)
		heuristics[len(row)]=best+heuristics[len(row)+1]

	for row in matrix:
		print row
	return matrix[-1][0]


if __name__=='__main__':
	import sys

	if len(sys.argv) is 1:
		print "please supply matrix file name"
		exit

	int_matrix=[ list([int(i) for i in x]) for x in importMatrix(sys.argv[1]," ")]
	root=createTree(int_matrix)
	res=findtarg(root,len(int_matrix)-1)
	vals=[i.val for i in res[0]]
	print vals, sum(vals)
	print len(int_matrix),res[1]
