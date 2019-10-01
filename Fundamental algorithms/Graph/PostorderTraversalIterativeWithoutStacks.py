"""Python3 program or postorder traversal """

# A Binary Tree Node 
# Utility function to create a 
# new tree node 
class newNode: 

	# Constructor to create a newNode 
	def __init__(self, data): 
		self.data = data 
		self.left = None
		self.right = None
		self.visited = False

def postorder(head) : 

	temp = head 
	while (temp and temp.visited == False): 

		# Visited left subtree 
		if (temp.left and
			temp.left.visited == False): 
			temp = temp.left 

		# Visited right subtree 
		elif (temp.right and
			temp.right.visited == False): 
			temp = temp.right 

		# Print node 
		else: 
			print(temp.data, end = " ") 
			temp.visited = True
			temp = head 
						
# Driver Code 
if __name__ == '__main__': 

	root = newNode(8) 
	root.left = newNode(3) 
	root.right = newNode(10) 
	root.left.left = newNode(1) 
	root.left.right = newNode(6) 
	root.left.right.left = newNode(4) 
	root.left.right.right = newNode(7) 
	root.right.right = newNode(14) 
	root.right.right.left = newNode(13) 
	postorder(root) 

# This code is contributed by 
# SHUBHAMSINGH10 
