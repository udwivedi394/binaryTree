class Node:
	def __init__(self,data,which="M"):
		self.data = data
		self.left = None
		self.right = None
		self.random = None
		self.which = which

#Time complexity: O(n)
#Space complexity: O(n)
def cloneBT(root):
	temp = root
	bHead = None
	stack = []
	hashmap = {None:None}

	#InOrder Traversal of tree and for each node create a new clone node
	#At this stage,No connections are being made in clone Nodes
	#Store the corresponding nodes in hashmap as {curNode:newCloneNode}
	while 1:
		while temp:
			stack.append(temp)
			temp = temp.left

		while temp==None and len(stack):
			temp = stack.pop()
			hashmap[temp] = Node(temp.data,"C")
			temp = temp.right

		if temp==None and len(stack)==0:
			break

	#Make connections in new Nodes, using the hashmap
	temp = root
	while 1:
		while temp:
			stack.append(temp)
			temp = temp.left

		while temp==None and len(stack):
			temp = stack.pop()
			#print temp.data,
			cloneNode = hashmap[temp]
			cloneNode.left = hashmap[temp.left]
			cloneNode.right = hashmap[temp.right]
			cloneNode.random = hashmap[temp.random]

			temp = temp.right

		if temp==None and len(stack)==0:
			break
	return hashmap[root]

#Time Complexity: O(n)
#Space Complexity: O(1)
def cloneBT02(root):
	temp = root
	stack = []
	
	#First traversal: Insert Clone node to left of each node
	while 1:
		while temp:
			stack.append(temp)
			temp = temp.left

		while temp==None and len(stack):
			temp = stack.pop()
			#Inserting clone node in left between the nodes
			leftNode = temp.left
			temp.left = Node(temp.data,"C")
			temp.left.left = leftNode

			temp = temp.right

		if temp==None and len(stack)==0:
			break

	#2nd Traversal: To assign the random pointers
	temp = root
	while 1:
		while temp:
			stack.append(temp)
			temp = temp.left

		while temp==None and len(stack):
			temp = stack.pop()
			#Assign left of random of current Node to random of left of current Node
			if temp.random:			
				temp.left.random = temp.random.left
			temp = temp.right

		if temp==None and len(stack)==0:
			break

	#3rd Travesal: Restore the trees to their linkages
	temp = root
	cloneRoot = root.left
	while 1:
		while temp:
			stack.append(temp)
	
			cloneNode = temp.left
			curNode = temp
			
			#Assign the left of left of curNode to the left of current Node
			curNode.left = curNode.left.left
			if curNode.right:
				cloneNode.right = curNode.right.left
			if cloneNode.left:
				cloneNode.left = cloneNode.left.left
			temp = temp.left

		while temp==None and len(stack):
			temp = stack.pop()
			temp = temp.right	

		if temp==None and len(stack)==0:
			break
	
	return cloneRoot

def inOrder(root):
	temp = root
	stack = []

	while 1:
		while temp:
			stack.append(temp)
			temp = temp.left

		while temp==None and len(stack):
			temp = stack.pop()
			print (temp.data,temp.random.data if temp.random else None,temp.which),
			temp = temp.right

		if temp==None and len(stack)==0:
			break
	
	return

root = Node(8)
l0 = root.left = Node(3)
l1 = root.left.left = Node(2)
l2 = root.left.left.left = Node(0)
l3 = root.left.left.right = Node(1)
l4 = root.left.right = Node(4)
r0 = root.right = Node(10)
r1 = root.right.left = Node(9)
r2 = root.right.right = Node(11)

root.random = l1
l0.random = r0
l2.random = l1
l3.random = l1
l4.random = root
r0.random = r1
r1.random = l4


print "Original Tree:"
inOrder(root)
print "\nClone Tree:"
cloneRoot = cloneBT02(root)
inOrder(root)
print
inOrder(cloneRoot)
