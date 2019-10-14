 

given array N of integers, find the most valuable contiguous subarray in the array
where the value of a subarray is defined as 
min(subarray) * sum(subarray)
return the value of such subarray

arr = [1,3,0,4,11,4,5,6]
helper_arr  [0,]
1   3  0
N  0  N

from collections import deque
def pass(arr):
res = [None] * len(arr)
helper = deque()
passing_sum = [0] * len(arr)

for i, val in enumerate(arr):
if not helper:
helper.append(val)
while val > arr[helper[-1]]:
helper.popright()
res[i] = helper[-1]
helper.appendright(i)
return res

def solve_helper(val,left_i,right_i):
return val * (val+ left_i[1]+right_i[1])

def solve(arr):
res = 0
left_pass = pass(arr)
right_pass = pass(arr[::-1])
for i, val in enumerate(arr):
curr = solve_helper( val, left_pass[i],  right_pass[i])
res = max(curr,res)
return res
