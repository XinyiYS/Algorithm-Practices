# 题目一：两个array， 算第一个array减去第二个array剩下的部分，元素的重复次数要考虑进去。
# 比如：A：[1，2，2，2，3]， B [2， 4] ， 最后回一个[1， 2，2，3]
# 题目二：一个array和一个K,回一个array，存array里所有长度为K的连续段的平均值。
# 比如：A：[1，2，3，4，5，6，7]， K：3，回一个[(1+2+3)/3, (2+3+4)/3, (3+4+5)/3,

# 1.
from collections import Counter
def removeBfromA(A, B):
	counterA = Counter(A)
	for b in B:
		if b in counterA:
			counterA[b] -= 1
			if counterA[b] == 0 : counterA.pop(b)

	res = []
	for a in A:
		if a in counterA:
			res += [a] 
			counterA[a] -= 1
			if counterA[a] == 0 : counterA.pop(a)

	return res
a = removeBfromA([1,2,2,2,3],[3,3,3,2,2,2,4])
print(a)



def runningAverage(arr, K):
	if not arr: return []
	if len(arr) < K: return [sum(arr) / len(arr)]
	res = []
	currSum = sum(arr[:K])
	res.append(currSum / K)
	l, r = 0, K # remove arr[l], add in arr[r]
	while r < len(arr):
		currSum -= arr[l]
		currSum += arr[r]
		res.append(currSum / K)
		l += 1
		r += 1
	return res

a = runningAverage([1,2,3,4,5,6,7],9)
print(a)


def runningAverage(arr, K):
	if not arr: return []
	res = []	
	currSum = l = r = 0
	while r < len(arr):
		while r - l < K and r < len(arr):
			currSum += arr[r]
			r += 1
		res.append(currSum / (r-l))
		currSum -= arr[l]
		l += 1
	return res

a = runningAverage([1,2,3,4,5,6,7],9)
print(a)

