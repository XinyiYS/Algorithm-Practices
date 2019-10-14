from bisect import bisect 
from numpy import random
a = list(random.randint(1,100,10))
print(a)
    # O(nlogn)
def lengthOfLIS(nums):
    parent = [-1] * len(nums)
    LIS = [nums[0]]
    LISindex = [0]

    for i in range(1, len(nums)):
        loc = bisect(LIS, nums[i])
        if LIS[loc-1] == nums[i] : continue
        if loc == len(LIS) :
            LIS.append(nums[i])
            LISindex.append(i)
        else:
            LIS[loc] = nums[i]
            LISindex[loc] = i
        parent[i] = LISindex[loc - 1]
        print(parent)

    actualLIS = []
    index = LISindex[-1]
    # while index != -1 :
    for i in range(len(LIS)):
        actualLIS.append(nums[index])
        index = parent[index]
    return len(LIS), actualLIS[::-1]

print(lengthOfLIS(a))