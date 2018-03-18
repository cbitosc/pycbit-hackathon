class BinaryTreeNode:
	#implments a complete binary tree
	def __init__(self, value, left=None, right=None):
		self.value=value;		
		self.nodes = [self.value]

	def __add__(self, other):
		#Nodes are added to the end of the tree as in CompleteBinaryTree
		self.nodes.append(other.value)
		#print("Node added at the end of the tree")


			

	def __sub__(self, other):
		#Since there are no constraints on how to delete nodes 
		#the specified node is deleted and the last node in the tree is put in its place
		if other.value not in self.nodes:
			print(str(other.value) + " is not in the tree")
		else:
			curPosition = self.nodes.index(other.value)
			self.nodes[curPosition] = self.nodes[-1]
			self.nodes.remove(self.nodes[-1])
			print("Node is " + "Deleted")
			if(len(self.nodes) == 0):
				root = None


	def printTree(self, root):
		#level order traversal
		if(root==None):
			print("Tree is empty")
		print("*********")
		for i in range(len(self.nodes)):
			print(self.nodes[i], end = " ")
		print(" ")	
		print("*********")
			
root = None
while(True):
	print("Select on option")
	print("1. Insert a node")
	print("2. Delete a node")
	print("3. Print the tree")
	choice = int(input())
	if(choice ==1):
		if(root==None):
			root = BinaryTreeNode(int(input('Enter the value to insert...')))
			print("Done inserting at the root")
		else:
			root + BinaryTreeNode(int(input('Enter the value to insert...')))
			print("Node is inserted")
	elif(choice == 2):
		root - BinaryTreeNode(int(input("Enter the node to be deleted")))
	elif(choice ==3):
		if(root==None):
			print("Tree is empty")
		else:
			print("The tree is ")
			root.printTree(root)
	else:
		print("Choose a valid option")



