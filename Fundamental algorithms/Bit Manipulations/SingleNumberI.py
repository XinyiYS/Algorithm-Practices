# Given a non-empty array of integers, every element appears twice except for one. Find that single one.

# https://leetcode.com/problems/single-number/description/


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        temp = 0
        for num in nums:
            temp = temp^num
        
        return temp
        