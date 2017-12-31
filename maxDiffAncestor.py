#Defining Binary Tree Node, it will have data, left pointer and right pointer
class Node:
	def __init__(self,data):
		self.data=data
		self.left=None
		self.right=None

#This function returns the maximum difference between any node and its ancestors
#Time complexity: O(n)
#Space Complexity: O(log n)
def maxDiff(root):
	#Stack used for inOrder Traversal
	stack = []
	#Stack used for tracking all ancestors of current node, including the current element
	ancestor = []
	temp = root

	#Initializing the maximum element with None
	maxi = None
	
	#Proceeding in inOrder fashion
	while 1:
		while temp:
			stack.append(temp)
			#Append the ancestor's data to the stack
			ancestor.append(temp.data)
			temp = temp.left

		while temp==None and len(stack):
			temp = stack.pop()

			#Pop the ancestors out of the ancestor stack, till the top is not equal to current temp
			while len(ancestor):
				if ancestor[-1]!=temp.data:
					ancestor.pop()
				else:
					break
			#Check the difference between all the available ancestors and current data
			#Traversing stack as list
			for key in ancestor:
				#print key, temp.data, key-temp.data
				#Get the current Max
				maxi = max(maxi, key-temp.data)
			temp = temp.right
		if temp==None and len(stack)==0:
			break
	return maxi

#Driver Program
root = Node(8)
root.left = Node(3)
root.left.left = Node(1)
root.left.right = Node(6)
root.left.right.left = Node(4)
root.left.right.right = Node(7)
root.right = Node(10)
root.right.right = Node(14)
root.right.right.left = Node(13)

print "The maximum difference between ancestors and nodes is",maxDiff(root)
