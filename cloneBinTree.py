class Node:
	def __init__(self,data):
		self.data = data
		self.left = None
		self.right = None
		self.random = None

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
			hashmap[temp] = Node(temp.data)
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

def inOrder(root):
	temp = root
	stack = []

	while 1:
		while temp:
			stack.append(temp)
			temp = temp.left

		while temp==None and len(stack):
			temp = stack.pop()
			print (temp.data,temp.random.data if temp.random else None),
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
cloneRoot = cloneBT(root)
inOrder(cloneRoot)
