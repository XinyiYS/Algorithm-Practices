# https://leetcode.com/problems/two-sum/description/

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        data = dict()
        for i,num in  enumerate(nums):
            if num in data:
                return [data[num],i]

            data[target-num] = i
        return

s = Solution()
a = s.twoSum( [2, 7, 11, 15],9)
print(a)
