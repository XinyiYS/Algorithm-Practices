
# pseudo in-place quickselect much more readable
def kth(arr,k):
	if not arr: return None
	pivot = arr.pop()
	smaller, bigger = [],[]
	while arr:
		a = arr.pop()
		if a < pivot: smaller.append(a)
		else:  bigger.append(a)
	smaller_count = len(smaller)
	bigger_count = len(bigger)
	if smaller_count < k - 1 :
		return kth(bigger,k - 1 - smaller_count)
	elif smaller_count == k - 1:
		return pivot
	else:
		return kth(smaller,k)

# in-place quickselect and partition for k-smallest
def findKthSmallest( nums, k):
 
    if nums:
    	l,r = 0 , len(nums) -1 
    	pivot = nums[r]
    	low = l
    	while l < r :
    		if nums[l] < pivot:
    			temp = nums[l]
    			nums[l] = nums[low]
    			nums[low] = temp
    			low += 1
    		l += 1
    	nums[low] , nums[r] = pivot, nums[low]
    	pos = low

    	if k > pos + 1:
    		return findKthSmallest(nums[pos+1:], k - (pos + 1))
    	elif k < pos + 1:
    		return findKthSmallest(nums[:pos],k)
    	else:
    		return nums[pos]
# import numpy as np 

N = 100
rounds = 100
from random import randint
arr = []
for i in range(N):
	arr.append(randint(1,3*N))
import time
start = time.time()
for i in range(rounds):
	#a = list(np.random.randint(1,3*N,N))
	# print(kth(a,5))
	# print(findKthSmallest(b,5))
	kth(arr,N//2)
end = time.time()
a = end - start

start = time.time()
for i in range(rounds):
	#a = list(np.random.randint(1,3*N,N))
	# print(kth(a,5))
	# print(findKthSmallest(b,5))
	findKthSmallest(arr,N//2)
end = time.time()
b = end - start
print('pseudo time: {}, avg {}. in-place time: {}, avg {}'.format(a, a//rounds,b , b//rounds) )



