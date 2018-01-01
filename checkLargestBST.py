class Node:
	def __init__(self,data):
		self.data = data
		self.left = None
		self.right = None

#This function returns the [MaxHeight,BSTstatusofCurrentNode]
def findLargestBST(root):
	if root==None:
		return None

	if root.left == None and root.right == None:
		return [1,True]

	leftCheck = 0
	rightCheck = 0

	if root.left:
		if root.left.data < root.data:
			leftCheck = findLargestBST(root.left)
		else:
			leftCheck = [0,False]
	if root.right:
		if root.right.data > root.data:
			rightCheck = findLargestBST(root.right)
		else:
			rightCheck = [0,False]

	print "I'm Node:",root.data,leftCheck,rightCheck
	
	if leftCheck[1] and rightCheck[1]:	
		return [leftCheck[0]+1,True] if leftCheck[0] > rightCheck[0] else [rightCheck[0]+1,True]

	return [leftCheck[0],False] if leftCheck[0] > rightCheck[0] else [rightCheck[0],False]
	
root = Node(5)
root.left = Node(2)
root.left.left = Node(1)
root.left.right = Node(3)
root.right = Node(4)

root1 = Node(50)
root1.left = Node(30)
root1.left.left = Node(5)
root1.left.right = Node(20)
root1.right = Node(60)
root1.right.left = Node(45)
root1.right.right = Node(70)
root1.right.right.left = Node(65)
root1.right.right.right = Node(80)

maxBST = findLargestBST(root)
print maxBST
