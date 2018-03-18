class BinaryTreeNode():

	def __init__(self, value=None):
		self.leftChild = None
		self.rightChild = None
		if value == None:
			self.value = None
		else:
			self.value = value

	def insertNode(self, data):
		if self.value:
			if data < self.value:
				if self.leftChild == None:
					self.leftChild = BinaryTreeNode(data)
					print("Node inserted successfully.\n\n")
				else:
					self.leftChild.insertNode(data)
			elif data > self.value:
				if self.rightChild == None:
					self.rightChild = BinaryTreeNode(data)
					print("Node inserted successfully.\n\n")
				else:
					self.rightChild.insertNode(data)
		elif self.value == None:
			self.value = data
			print("Node inserted successfully.\n\n")


	def search(self, data, parent=None):
		if data < self.value:
			if self.leftChild == None:
				return None, None
			return self.leftChild.search(data, self)
		elif data > self.value:
			if self.rightChild == None:
				return None, None
			return self.rightChild.search(data, self)
		elif data == self.value:
			return self, parent
		else:
			return None, None

	def children_count(self):
		count = 0
		if self.leftChild:
			count += 1
		if self.rightChild:
			count += 1
		return count

	def deleteNode(self, data):

		node, parent = self.search(data)
		if (node == None and parent == None):
			print("Entered node does not exist to delete.\n\n")
			return

		if (parent == None and node.leftChild == None and node.rightChild == None):
			node.value = None
			print("Node deleted successfully.\n\n")
			return

		if node != None:
			child_count = node.children_count()

		if child_count == 0:
			if parent:
				if parent.leftChild == node:
					parent.leftChild = None
				else:
					parent.rightChild = None
				print("Node deleted successfully.\n\n")
				del node
			else:
				parent.value = None
				print("Node deleted successfully.\n\n")

		elif child_count == 1:
			if node.leftChild:
				n = node.leftChild
			else:
				n = node.rightChild
			if parent:
				if parent.leftChild == node:
					parent.leftChild = n
				else:
					parent.rightChild = n
				print("Node deleted successfully.\n\n")
				del node
			else:
				self.leftChild = n.leftChild
				self.rightChild = n.rightChild
				self.value = n.value
				print("Node deleted successfully.\n\n")

		else:
			parent = node
			successor = node.rightChild
			while successor.leftChild:
				parent = successor
				successor = successor.leftChild
			node.value = successor.value
			if parent.leftChild == successor:
				parent.leftChild = successor.rightChild
				print("Node deleted successfully.\n\n")
			else:
				parent.rightChild = successor.rightChild
				print("Node deleted successfully.\n\n")

	def printInorder(self):
		try:
			if self:
				if self.leftChild:
					self.leftChild.printInorder()

				print(self.value)

				if self.rightChild:
					self.rightChild.printInorder()
		except:
			print("Unexpected error! Please try again.")

def doMain():
    flag = True
    root = BinaryTreeNode()
    while flag:
        opt = input("Enter + to add a node.\nEnter - to delete a node.\nEnter = to print tree(Inorder traversal).\nEnter 0 to quit.\nOption: ")

        if(opt == "+"):
            data = input("Enter node to insert: ")
            root.insertNode(data)
        elif(opt == "-"):
            data = input("Enter node to delete: ")
            if root == None:
                print("No data to delete.\n")
            else:
                root.deleteNode(data)
        elif(opt == "="):
            root.printInorder()
        elif(opt == "0"):
            flag = False
        else:
            print("Invalid option. Please re-enter.")

doMain()