# Given a non-empty array of integers, every element appears three times except for one, which appears exactly once. Find that single one.

# https://leetcode.com/problems/single-number-ii/description/
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int\
        """
        ones, twos = 0, 0
        for num in nums:
            ones = ones ^ num & ~ twos
            twos = twos ^ num & ~ ones
        return ones
