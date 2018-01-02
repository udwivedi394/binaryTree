class Node:
	def __init__(self,data):
		self.data=data
		self.left=None
		self.right=None

#Constructs the SpecialBinary Tree as per the postOrder traversal data given in the array, pre 
#For every node, whether it is 'L'-leaf node or 'N'-Non-leaf node is given preLN
#Given every Node has either 0 or 2 children
def specialTree(pre,preLN):
	stack = []
	root = None

	for i in range(len(pre)):
		#If it is non-leaf node, then connect it with left of top of stack and push it in the stack
		if preLN[i]=='N':
			if root == None:
				newNode = root = Node(pre[i])
			else:
				newNode = Node(pre[i])
				stack[-1].left = newNode
			stack.append(newNode)
		#If it is Leaf node, then connect is with left and right of top of stack
		else:
			lastNode = stack[-1]
			if lastNode.left == None:
				lastNode.left = Node(pre[i])
			#After connection at right, pop the top node from stack
			elif lastNode.right == None:
				lastNode.right = Node(pre[i])
				stack.pop()
	return root

def inOrder(root):
	if root == None:
		return None
	if root.left:
		inOrder(root.left)
	print root.data,
	
	if root.right:
		inOrder(root.right)
	return

pre = [10,30,20,5,15]
preLN = ['N','N','L','L','L']
root = specialTree(pre,preLN)
inOrder(root)
