# 57. Insert Interval
# https://leetcode.com/problems/insert-interval/description/

# Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

# You may assume that the intervals were initially sorted according to their start times.

# Example 1:
# Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
# Output: [[1,5],[6,9]]

# Example 2:
# Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# Output: [[1,2],[3,10],[12,16]]
# Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].


# 1. binary search for the beginning and end intervals
# 	start, end = new_interval
# 	1.1 
# 		binary search for the interval that contains start, if exisit
# 		if does not exist: find the first interval with a larger start
		
# 		first = binary_search(start)
# 	1.2 
# 		since the intervals given are non-overlapping and sorted in start times,
# 		their end times are necessarily sorted, too
# 		binary search for the interval that contains end, if exist
# 		if does not exist: find the last interval with a smaller end  
# 		last = binary_search(end)
# 2.  
# 	2.1 
# 		if last - first >= 0:
# 			merge all the intervals in between these
# 			merged = [ [min(start, first.start), max(end, last.end)] ]
# 	2.2 
# 		else: # meaning completely no overlapping at all
# 		if it covers none of the original intervals, we need to insert itself,
# 		take care of this edge case
# 3. 
# 	return intervals[:first] + merged + intervals[last+1:]

class Solution:
    def insert(self, intervals, newInterval):
    	if not intervals : return [newInterval]
    	start, end = newInterval
    	first, last = self.binarySearchStart(intervals, start), self.binarySearchEnd(intervals, end) - 1
    	if last >= first :
    		merge = [[min(start, intervals[first][0]), max(end, intervals[last][1])]]
    		intervals = intervals[:first] + merge + intervals[last+1:]
    	else:
    		intervals.insert(first, newInterval)

    	return intervals

    def binarySearchStart(self, intervals, start):
    	l, h = 0, len(intervals) - 1
    	while l < h:
    		mid = (l+h)//2
    		if intervals[mid][1] < start:
    			l = mid + 1
    		else:
    			h = mid
    	return l + int(intervals[l][1] < start)

    def binarySearchEnd(self, intervals, end):
    	l, h = 0, len(intervals) - 1
    	while l < h:
    		mid = (l+h+1)//2
    		if intervals[mid][0] <= end:
    			l = mid
    		else:
    			h = mid - 1
    	return l + int(intervals[l][0] <= end)


intervals = [[1,2],[3,5],[8,10],[12,16]]
newInterval = [4,5]
print('original: ', intervals)
print('new: ',newInterval)
s = Solution()
res = s.insert(intervals,newInterval)
print(res)


        

