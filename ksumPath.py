class Node:
	def __init__(self,data):
		self.data = data
		self.left = None
		self.right = None

#Prints all the paths in the binary Tree with sum equal to k
def ksumPaths(root,k):
	#Used for inOrder traversal
	stack = []

	#Store the path to current Node, on top there will be always the sum of the stack
	pathStack = []
	temp = root

	while 1:
		while temp:
			stack.append(temp)
			#Append the node in stack
			if len(pathStack)==0:
				pathStack.append(temp)
				topSum = 0
			else:
				topSum = pathStack.pop()
				pathStack.append(temp)
			#Append the sum of the stack on top
			pathStack.append(temp.data+topSum)
			temp = temp.left
		
		while temp==None and len(stack):
			temp = stack.pop()
			#print temp.data,"->",
	
			#Safely takeout the sum
			topSum = pathStack.pop()

			#Start popping out the stack, till the current node is visible on top
			while pathStack[-1] != temp:
				#Substract the topSum as well, for every node popped out
				topSum -= pathStack.pop().data

			#Keep safe the topSum, it will be going on top as it is, before leaving this block
			tempSum = topSum
			i = 0

			#Start from bottom of stack
			while i < len(pathStack):
				#If tempSum is equal to k, print the stack from here on
				if tempSum == k:
					for j in range(i,len(pathStack)):
						print pathStack[j].data,
					print
				#If not decrement the current node data from tempSum and move on
				tempSum -= pathStack[i].data
				i += 1
			
			#Put the topSum on top
			pathStack.append(topSum)
			temp = temp.right

		if temp==None and len(stack)==0:
			break
	return

root = Node(1)
root.left = Node(3)
root.left.left = Node(2)
root.left.right = Node(1)
root.left.right.left = Node(1)
root.right = Node(-1)
root.right.left = Node(4)
root.right.left.left = Node(1)
root.right.left.right = Node(2)
root.right.right = Node(5)
root.right.right.right = Node(6)

ksumPaths(root,5)
