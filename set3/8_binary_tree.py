class BinaryTreeNode:
	def __init__(self, value, left=None, right=None):
		self.value=value;
		self.left = left
		self.right = right

	def __add__(self, other):
		if(self.left == None):
			self.left = other
			print("Added " +str(other.value) + " as left child of " + str(self.value))
		elif(self.right == None):
			self.right = other
			print("Added " +str(other.value) + " as right child of " + str(self.value))
		else:
			print("The current node is not vacant")

	def __sub__(self, other):
		if(self.left == other):
			self.left = None
			print("Deleted the left node of " + str(self.value))
		elif(self.right == other):
			self.right = None
			print("Deleted the right node of" + str(self.value))
		else:
			print(str(other.value) +" is not a child of " + str(self.value))

	def printTree(self, root):
		#inorder traversal of the tree
		print(root.value)
		if(root.left !=None):
			self.printTree(root.left)
		if(root.right!=None):
			self.printTree(root.right)

root = BinaryTreeNode(1)
a = BinaryTreeNode(2)
b = BinaryTreeNode(3)
c = BinaryTreeNode(4)

root+a#a is added as left child of root
root+b#b is added as right child of root
b + c#c is added as the left child of b

'''Tree is now
      1
     /  \
    2    3
   /
  4
'''

root.printTree(root)

b-c#c is removed as the left child of b

'''Tree is now
      1
     /  \
    2    3
'''

root.printTree(root)



