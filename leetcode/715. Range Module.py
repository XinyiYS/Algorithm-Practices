# 715. Range Module
# https://leetcode.com/problems/range-module/description/

# A Range Module is a module that tracks ranges of numbers. Your task is to design and implement the following interfaces in an efficient manner.

# addRange(int left, int right) Adds the half-open interval [left, right), tracking every real number in that interval. Adding an interval that partially overlaps with currently tracked numbers should add any numbers in the interval [left, right) that are not already tracked.

# queryRange(int left, int right) Returns true if and only if every real number in the interval [left, right) is currently being tracked.

# removeRange(int left, int right) Stops tracking every real number currently being tracked in the interval [left, right).

# Example 1:
# addRange(10, 20): null
# removeRange(14, 16): null
# queryRange(10, 14): true (Every number in [10, 14) is being tracked)
# queryRange(13, 15): false (Numbers like 14, 14.03, 14.17 in [13, 15) are not being tracked)
# queryRange(16, 17): true (The number 16 in [16, 17) is still being tracked, despite the remove operation)

# Note:
# A half open interval [left, right) denotes all real numbers left <= x < right.
# 0 < left < right < 10^9 in all calls to addRange, queryRange, removeRange.
# The total number of calls to addRange in a single test case is at most 1000.
# The total number of calls to queryRange in a single test case is at most 5000.
# The total number of calls to removeRange in a single test case is at most 1000.


# intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
# toRemove = [4,8]
# # Output: [[1,2],[3,10],[12,16]]

# 	[[1,2],[3,4],[8,10],[12,16]]


# See LC 57 for a similar idea implemented using binary search to achieve O(log N)
# # 57. Insert Interval
# # https://leetcode.com/problems/insert-interval/description/

# Here we can carry out very similar implementations
# 1. addRange essentially the same to insert interval
# 		addRange involves: intervals[:first] + merged + intervals[last+1:]
# 2. removeRange(start, end) is the reverse operation to addRange
# 		removeRange involves: intervals[:first] + update(intervals[first]) + update(intervals[last]) + intervals[last+1:]

# 3. queryRange(start, end): 
# 		binary search for the interval that contains the start point
# 		check if this interval contains the end

# Note: all intervals will be non-overlapping and sorted according to start points at all times.

class RangeModule:

	def __init__(self):
		self.intervals = []

	def addRange(self, left: int, right: int) -> None:
		toInsert = [left, right]
		self.insertInterval(toInsert)
		print(self.intervals)

	def queryRange(self, left: int, right: int) -> bool:
		# print(self.intervals, left, right)
		interval = self.searchQueryLeft(left)
		if interval: return interval[1] >= right
		else: return False

	def searchQueryLeft(self, left):
		l, h = 0, len(self.intervals) - 1
		while l < h:
			mid = (l+h)//2
			if self.intervals[mid][1] < left:
				l = mid + 1
			else:
				h = mid 

		return self.intervals[l] if l < len(self.intervals) and self.intervals[l][0] <= left <= self.intervals[l][1] else None

	def removeRange(self, left: int, right: int) -> None:
		toRemove = [left, right]
		self.removeInterval(toRemove)
		print(self.intervals)
		return

	def removeInterval(self, toRemove):
		if not self.intervals : return
		start, end = toRemove
		first, last = self.binarySearchStart(start), self.binarySearchEnd(end) - 1 
		if last >= first :
			updated = []
			if self.intervals[first][0] < start:
				updated += [self.intervals[first][0], start],

			if self.intervals[last][1] > end:
				updated += [end, self.intervals[last][1]],

			self.intervals = self.intervals[:first] + updated + self.intervals[last+1:]

	def insertInterval(self, toInsert):
		if not self.intervals : self.intervals = [toInsert]
		start, end = toInsert
		first, last = self.binarySearchStart(start), self.binarySearchEnd(end) - 1 

		if last >= first :
			merge = [[min(start, self.intervals[first][0]), max(end, self.intervals[last][1])]]
			self.intervals = self.intervals[:first] + merge + self.intervals[last+1:]
		else:
			self.intervals.insert(first, toInsert)

	def binarySearchStart(self, start):
		l, h = 0, len(self.intervals) - 1
		while l < h:
			mid = (l+h)//2
			if self.intervals[mid][1] < start:
				l = mid + 1
			else:
				h = mid
		return l + int(self.intervals[l][1] < start)

	def binarySearchEnd(self, end):
		l, h = 0, len(self.intervals) - 1
		while l < h:
			mid = (l+h+1)//2
			if self.intervals[mid][0] <= end:
				l = mid
			else:
				h = mid - 1
		return l + int(self.intervals[l][0] <= end)

rm = RangeModule()
rm.addRange(10, 20)
rm.removeRange(14, 16)
rm.removeRange(12, 17)
rm.addRange(13,16)
rm.removeRange(14,15)

a = rm.queryRange(10, 11)#: true (Every number in [10, 14) is being tracked)
print(a)
a = rm.queryRange(13, 14)#:false (Numbers like 14, 14.03, 14.17 in [13, 15) are not being tracked)
print(a)
a = rm.queryRange(16, 17)#: true (The number 16 in [16, 17) is still being tracked, despite the remove operation)
print(a)




