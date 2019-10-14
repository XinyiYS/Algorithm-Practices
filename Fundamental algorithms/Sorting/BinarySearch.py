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

