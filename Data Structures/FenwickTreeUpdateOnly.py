# Python3 program to demonstrate Range 
# Update and PoQueries Without using BIT 

# Updates such that getElement() gets an 
# increased value when queried from l to r. 
def update(arr, l, r, val): 
	arr[l] += val 
	if r + 1 < len(arr): 
		arr[r + 1] -= val 

# Get the element indexed at i 
def getElement(arr, i): 
	
	# To get ith element sum of all the elements 
	# from 0 to i need to be computed 
	res = 0
	for j in range(i + 1): 
		res += arr[j] 

	return res 

# Driver Code 
if __name__ == '__main__': 
	arr = [0, 0, 0, 0, 0] 
	n = len(arr) 

	l = 2
	r = 4
	val = 2
	update(arr, l, r, val) 

	# Find the element at Index 4 
	index = 4
	print("Element at index", index, 
		"is", getElement(arr, index)) 

	l = 0
	r = 3
	val = 4
	update(arr, l, r, val) 

	# Find the element at Index 3 
	index = 3
	print("Element at index", index, 
		"is", getElement(arr, index)) 

# This code is contributed by PranchalK 
