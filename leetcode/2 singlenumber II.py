# https://leetcode.com/problems/single-number-ii/discuss/43294/Challenge-me-thx
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int\
        """
        ones, twos = 0, 0
        for num in nums:
            # ones is used to hold the numbers that have up to now appeared once
            # and when a number appears a third time, the ones is updated to zero by the following way:
                # currently the ones for this number is 0, the twos for this number is 1
                # ones ^ num gives the num itself, then num ^ ~num gives 0
                # effectively counts the num thrice and clear to 0
            ones = ones ^ num & ~twos

            # twos is used to hold the numbers that have up to now appeared twice
            # and when any number appears a third time, the twos is updated to zero
            twos = twos ^ num & ~ ones
        return ones
# s = Solution()
