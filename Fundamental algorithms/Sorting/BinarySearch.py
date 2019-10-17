def binarySearch(arr, target, low=None, high=None):
	l = low if low else 0 
	h = high if high else len(arr) - 1

	while l < h:
		mid = (l + h + 1)//2 
		# if evaluate(mid) <= target:
		if arr[mid] <= target:
			l = mid
		else:
			h = mid - 1
	return l

def binarySearch(arr, target, low=None, high=None, L = False):
	l = low if low else 0 
	h = high if high else len(arr) - 1

	while l < h:
		mid = (l + h + 1)//2 
		# if evaluate(mid) <= target:
		if arr[mid] <= target:
			l = mid
		else:
			h = mid - 1
	if L:
		return l + int(arr[l] < target)
	else:
		return l


# import numpy as np
# a = sorted(np.random.randint(1, 100, 20))
a = [1,2,5,6,7,9]
l = binarySearch(a,1, L=True)
print(l, a[l])

r = binarySearch(a,5)
print(r, a[r])
print(r - l + 1)



def binarySearch(arr, target):
	low, high = 0, len(arr) - 1
	while low < high:
		mid = (low + high + 1) //2
		if (evaluate(mid) <= mid):
			low = mid
		else:
			high = mid - 1
	return low



# int begin = LOWER_BOUND;
# int end = UPPER_BOUND;
# while (begin < end){
#     int mid = (begin + end)/2;
#     if(evaluate(mid) < target){
#         begin = mid + 1;
#     } else {
#         end = mid;
#     }
# }


