# 56. Merge Intervals
# https://leetcode.com/problems/merge-intervals/description/	

# Given a collection of intervals, merge all overlapping intervals.

# Example 1:

# Input: [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
# Example 2:

# Input: [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.


# 1. sort according to the starting times
# 2. iterate the sorted array of intervals and merge
# 	while currEnd >= interval[i+1].start
# 		currEnd = interval[i+1].end
# 		i+=1

# 	res.append([currBegin, currEnd])
# 	i+=1
# 	currBegin, currEnd = interval[i]

class Solution:
    def merge(self, intervals):
    	intervals.sort(key=lambda x:x[0]) # then sort the intervals by start
    	res = []
    	i = 0
    	while i < len(intervals):
    		begin, end = intervals[i]
    		while i < len(intervals)-1 and end >= intervals[i+1][0]:
    			i += 1
    			end = max(end,intervals[i][1])

    		res.append([begin, end])
    		i += 1

    	return res

s = Solution()
intervals = [[1,4],[2,5],[2,3]]
res = s.merge(intervals)
print(res)