import binaryHeap as bHeap
import binaryHeapUtility as bHeap2

class bTree:
	def __init__(self,key):
		self.data = key
		self.left = None
		self.right = None

def findHeightofTree(node):
	if node.left == None and node.right == None:
		return 1

	lheight = 0
	rheight = 0
	if node.left:
		lheight = 1 + findHeightofTree(node.left)

	if node.right:
		rheight = 1 + findHeightofTree(node.right)

	return max(lheight, rheight)

def convertTreeToHeap(arr, root, cur_index=0):
	arr[cur_index] = root.data
	if root.left:
		left_index = bHeap.left_child(cur_index, arr)
		arr[left_index] = root.left.data
		convertTreeToHeap(arr, root.left, left_index)
	if root.right:
		right_index = bHeap.right_child(cur_index, arr)
		arr[right_index] = root.right.data
		convertTreeToHeap(arr, root.right, right_index)
	return

def levelOrder(root):
	queue = []
	temp = root
	queue.append(temp)
	while len(queue):
		#count the number of nodes at current level
		n = len(queue)
		
		while n:
			temp = queue.pop(0)
		
			if temp.left:
				queue.append(temp.left)
			if temp.right:
				queue.append(temp.right)
			print temp.data,
			n -= 1
		print
	return	
#Prints the left most and right most nodes at each level
def printLeftRightMost(root):
	#Initialise the queue
	queue = []
	temp = root

	#Flag to identify left most node
	left = False

	#Enqueue the root node to the queue, stucture is [level_of_node, node]
	queue.append(temp)
	print
	while len(queue):
		n = nodeCount = len(queue)

		while n:
			temp = queue.pop(0)
		
			#Store the nodes along with their levels in queue
			if temp.left:
				queue.append(temp.left)
			if temp.right:
				queue.append(temp.right)

			if left and n==nodeCount:
				if nodeCount!=1:
					print temp.data,
				left = False
			if left==False and n==1:
				print temp.data
				left = True
			n -= 1
	return

#Prints the left most and right most nodes at each level
def printLeftRightMostAlternate(root):
	#Initialise the queue
	queue = []
	temp = root

	#Flag to identify left most node
	left = False
	leftNode = None

	alternate = False
	#Enqueue the root node to the queue, stucture is [level_of_node, node]
	queue.append([1, temp])
	print
	while len(queue):
		node = queue.pop(0)
		level = node[0]
		temp = node[1]
		
		#Store the nodes along with their levels in queue
		if temp.left:
			queue.append([level+1, temp.left])
		if temp.right:
			queue.append([level+1, temp.right])

		#if current node is left most node
		if left:
			if alternate:
				print temp.data,
				left = False
				#store the leftmost address in leftNode
				leftNode = temp
			elif len(queue)==0:
				print temp.data

		#If the level of next node in queue is greater than current level, then this is the right most node
		if len(queue) and queue[0][0] > level:
			#This condition will be true when there is only 1 node at current level
			if leftNode != temp:
				if alternate==False:
					print temp.data,
					alternate = True
				else:
					alternate = False
			#The next node is going to be left Most, so set it True
			left = True
	return

#Prints the left most and right most nodes at each level
def printLeftRightMostAlternate02(root):
	#Initialise the queue
	queue = []
	temp = root

	#Flag to identify left most node
	left = False

	#Enqueue the root node to the queue, stucture is [level_of_node, node]
	queue.append(temp)
	print
	while len(queue):
		n = nodeCount = len(queue)

		while n:
			temp = queue.pop(0)
		
			#Store the nodes along with their levels in queue
			if temp.left:
				queue.append(temp.left)
			if temp.right:
				queue.append(temp.right)
			
			#Print the left most node
			if left and n==nodeCount:
				print temp.data,
			#Print the right most node
			if left==False and n==1:
				print temp.data,
			n -= 1
		left ^= True
	return
root = bTree(1)
root.left = bTree(2)
root.left.left = bTree(4)
root.left.right = bTree(5)
root.right = bTree(3)
root.right.left = bTree(6)
root.right.right = bTree(7)
root.right.right.right = bTree(8)
root.right.right.right.left = bTree(9)
root.right.right.right.left.right = bTree(10)

#height = findHeightofTree(root)
#arr = [None]*(2**height-1)
#convertTreeToHeap(arr,root)
#bHeap2.printGivenHeap(arr)

root2 = bTree(1)
root2.left = bTree(2)
root2.right = bTree(3)
root2.left.left = bTree(4)
root2.left.right = bTree(5)
root2.left.left.left = bTree(8)
root2.left.left.right = bTree(9)
root2.left.right.left = bTree(10)
root2.left.right.left.left = bTree(39)
root2.left.right.left.left.left = bTree(40)
root2.left.right.left.left.left.right = bTree(41)
root2.left.right.left.left.left.right.left = bTree(42)
root2.left.right.right = bTree(11)
root2.right.left = bTree(6)
root2.right.right = bTree(7)
root2.right.left.left = bTree(12)
root2.right.left.right = bTree(13)
root2.right.right.left = bTree(14)
root2.right.right.right = bTree(15)
root2.right.right.right.left = bTree(30)
root2.right.right.right.right = bTree(31)
root2.right.right.right.right.left = bTree(32)
#root2.right.right.right.right.right = bTree(32)

#height = findHeightofTree(root2)
#arr = [None]*(2**height-1)
#convertTreeToHeap(arr,root2)
#bHeap2.printGivenHeap(arr)

levelOrder(root2)
printLeftRightMost(root2)
printLeftRightMostAlternate02(root2)
