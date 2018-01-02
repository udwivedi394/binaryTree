class Node:
	def __init__(self,data):
		self.data = data
		self.left = None
		self.right = None

#Prints the Level Order traversal of binary Tree
#Prints the Bottom View of Binary Tree
def bottomView(root):
	temp = root
	#Lookup, {pos: NodeData}
	hashmap = {}

	#Node in queue is of form, [Node, horizontal position wrt root]
	queue = [[temp,0]]

	#Leftmost Horizontal position
	mini = 0
	#Rightmost horizontal position
	maxi = 0

	#Do the levelOrder traversal
	while len(queue):
		n = len(queue)

		while n:
			temp = queue.pop(0)
			node = temp[0]
			pos = temp[1]
			
			#For every node to be enqueue position is left->current_pos-1, right->current_pos+1
			if node.left:
				queue.append([node.left,pos-1])
			if temp[0].right:
				queue.append([node.right,pos+1])
			
			hashmap[pos] = node.data
			mini = min(mini, pos)
			maxi = max(maxi, pos)

			print node.data,
			n -= 1
		print

	#Print the bottom View spectrum, from hashmap
	print "The bottom View:",
	for i in range(mini,maxi+1):
		print hashmap[i],

	return

root = Node(20)
root.left = Node(8)
root.left.left = Node(5)
root.left.right = Node(3)
root.left.right.left = Node(10)
root.left.right.right = Node(14)
root.right = Node(22)
root.right.left = Node(4)
root.right.right = Node(25)

bottomView(root)
