class Node:
	def __init__(self,data):
		self.data = data
		self.left = None
		self.right = None

#Time complexity: O(n)
#This function returns the [MaxHeight,BSTstatusofCurrentNode,minimum of subtree,maximum of subtree]
def findLargestBSTUtil(root):
	if root==None:
		return [0,False,None,None]

	#If current node is leaf node, count is 1, it is a BST, max and min is the data iteself
	if root.left == None and root.right == None:
		return [1,True,root.data,root.data]

	#Initialize the leftCheck and RightCheck of the tree
	leftCheck = [0,True,root.data,root.data]
	rightCheck = [0,True,root.data,root.data]

	#If left subtree is present
	if root.left:
		#Check if the immediate data of left subtree satisfies the BST condition
		if root.left.data < root.data:
			leftCheck = findLargestBSTUtil(root.left)
		else:
			#Otherwise Set the status as False
			leftCheck = [0,False,None,None]
	
	#Same as left Subtree
	if root.right:
		if root.right.data > root.data:
			rightCheck = findLargestBSTUtil(root.right)
		else:
			rightCheck = [0,False,None,None]

	print "I'm Node:",root.data,leftCheck,rightCheck
	
	#If status of both the left and right subtree is BST, then
	if leftCheck[1] and rightCheck[1]:
		#Check if max of leftsubtree is less and min of rightsubtree is greater than current Node data
		if leftCheck[3] <= root.data and rightCheck[2] >= root.data:
			#Return the sum of nodes of left and right subtree + 1, status is BST, mini is the minimum from leftsubtree
			#Max is the maximum from rightsubtree
			return [leftCheck[0]+rightCheck[0]+1,True,leftCheck[2],rightCheck[3]]
	#If any of above condition fails, then from here the BST status is false,
	#And the tree which has max number of nodes will be returned
	leftCheck[1] = rightCheck[1] = False
	return leftCheck if leftCheck[0] > rightCheck[0] else rightCheck

def findLargestBST(root):
	return findLargestBSTUtil(root)[0]

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

root1 = Node(50)
root1.left = Node(10)
root1.left.left = Node(5)
root1.left.right = Node(20)
root1.right = Node(60)
root1.right.left = Node(55)
root1.right.right = Node(70)
root1.right.left.left = Node(45)
root1.right.right.left = Node(65)
root1.right.right.right = Node(80)

maxBST = findLargestBST(root)
print maxBST
