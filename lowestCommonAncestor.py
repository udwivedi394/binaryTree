class bTree:
	def __init__(self,data):
		self.data = data
		self.left = None
		self.right = None

#Time Complexity: O(n), Space Comlexity: O(log n), 2 Tree traversal
def lca(root,key1,key2):
	path1 = findPath(root,key1)
	path2 = findPath(root,key2)
	
	if path1==None or path2==None:
		print "Keys not Found"
		return None

	print "Path1:",
	for cur in path1:
		print cur.data,
	print

	print "Path2:",
	for cur in path2:
		print cur.data,
	print


	i = 0
	while path1[i] == path2[i]:
		i += 1

	return path1[i-1]

#If found returns the list of path of nodes
def findPath(root,key,path=None):
	if root==None:
		return None
	
	if path==None:
		path=[root]

	if root.data==key:
		return path
	
	lpath = path+[root.left]
	left = findPath(root.left,key,lpath)
	rpath = path+[root.right]
	right = findPath(root.right,key,rpath)

	return max(left,right)

#Time complexity: O(n), Space Complexity: O(1), 1 Tree traversal
#Although better, problem with this solution is that it assumes both the values are present in tree
def lca02(root,key1,key2):
	if root == None:
		return None
	
	if root.data == key1 or root.data == key2:
		return root

	left = lca02(root.left,key1,key2)
	right = lca02(root.right,key1,key2)

	if left and right:
		return root

	return left if left else right

def findDist(root,key1,key2):
	commonNode = lca(root,key1,key2)
	
	if commonNode==None:
		print "Both or one of the given nodes not present in given node"
		return None

	path1 = findPath(commonNode,key1)
	path2 = findPath(commonNode,key2)
	
	return len(path1)+len(path2)-2


root2 = bTree(1)
root2.left = bTree(2)
root2.left.left = bTree(4)
root2.left.left.left = bTree(8)
root2.left.left.right = bTree(9)
root2.left.right = bTree(5)
root2.left.right.right = bTree(19)
root2.right = bTree(3)
root2.right.left = bTree(6)
root2.right.right = bTree(7)
root2.right.left = bTree(10)
root2.right.right.left = bTree(12)
root2.right.right.right = bTree(15)

common = lca02(root2,8,15)
print
if common:
	print common.data

print findDist(root2,9,15)
