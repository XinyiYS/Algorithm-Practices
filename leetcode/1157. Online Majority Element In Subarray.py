# 1157. Online Majority Element In Subarray
# https://leetcode.com/problems/online-majority-element-in-subarray/description/

# Implementing the class MajorityChecker, which has the following API:

# MajorityChecker(int[] arr) constructs an instance of MajorityChecker with the given array arr;

# int query(int left, int right, int threshold) has arguments such that:
# 0 <= left <= right < arr.length representing a subarray of arr;
# 2 * threshold > right - left + 1, ie. the threshold is always a strict majority of the length of the subarray
# Each query(...) returns the element in arr[left], arr[left+1], ..., arr[right] that occurs at least threshold times, or -1 if no such element exists.

# Example:
# MajorityChecker majorityChecker = new MajorityChecker([1,1,2,2,1,1]);
# majorityChecker.query(0,5,4); // returns 1. [1,1,2,2,1,1]
# majorityChecker.query(0,3,3); // returns -1 [1,1,2,2]
# majorityChecker.query(2,3,2); // returns 2. [2,2]

# Constraints:
# 1 <= arr.length <= 20000
# 1 <= arr[i] <= 20000
# For each query, 0 <= left <= right < len(arr)
# For each query, 2 * threshold > right - left + 1
# The number of queries is at most 10000

from collections import Counter, defaultdict
from bisect import bisect, bisect_left
class MajorityChecker:

    def __init__(self, arr):
    	self.freq_counter, self.indices_map, self.sorted_keys = self.preprocess(arr)

    def query(self, left: int, right: int, threshold: int) -> int:
        remaining = right - left + 1
        for key in self.sorted_keys:
            if remaining < threshold: return -1
            numOccur = self.findOccurr(key, left, right)
            if numOccur >= threshold: 
                return key
            else: 
                remaining -= numOccur
        return

    def preprocess(self, arr):
        freq_count, indices_map = Counter(), defaultdict(list)
        for i, num in enumerate(arr):
            freq_count[num] += 1
            indices_map[num].append(i)

        key_value_pairs = sorted(freq_count.items(), key=lambda x:x[1], reverse=True)
        sorted_keys = [key_value_pair[0] for key_value_pair in key_value_pairs]
        return freq_count, indices_map, sorted_keys

    def findOccurr(self, key, left, right):
        # to search of num of occurrences of the key, in arr[left:right+1]
        indices = self.indices_map[key]
        r, l = self.binarySearch(indices, right), self.binarySearch(indices, left, L = True) 
        return r - l + 1

    def binarySearch(self, indices, target, L=False):
        l, h = 0, len(indices) - 1
        while l < h:
            mid = (l + h + 1) // 2
            if indices[mid] <= target:  
                l = mid
            else:
                h = mid - 1
        return  l + (L and int(indices[l] < target))


majorityChecker = MajorityChecker([1,1,2,2,1,1]);
c = majorityChecker.query(2,3,2);# // returns 2
print(c)



