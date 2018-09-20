# https://leetcode.com/problems/3sum/description/

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # check if length is long enough
        if len(nums)<3:
            return []

        # create a occurrence dict for the counts
        occurrences = dict()
        results = []
        for num in nums:
            if num not in occurrences:
                occurrences[num] = 1
            else:
                occurrences[num] += 1

        # check for [0,0,0] case
        if 0 in occurrences and occurrences[0] >= 3 :
            results.append([0,0,0])

        # used for duplicates
        result_tuple_set = set()

        # iterate through positive number pairs, negative number pairs and pos-negative number pairs
        pos,neg = set(),set()
        for num in nums:
            if num > 0:
                pos.add(num)
            elif num < 0:
                neg.add(num)

        for p1 in pos:
            for p2 in pos - set([p1]):
                if (-p1-p2) in occurrences:
                    if tuple(sorted([p1,p2,-p1-p2])) not in result_tuple_set:
                        result_tuple_set.add(tuple(sorted([p1,p2,-p1-p2])))
                        results.append([p1,p2,-p1-p2])

        for n1 in neg:
            for n2 in neg - set([n1]):
                if -(n1+n2) in occurrences:
                    if tuple(sorted([n1,n2,-n1-n2])) not in result_tuple_set:
                        result_tuple_set.add(tuple(sorted([n1,n2,-n1-n2])))
                        results.append([n1,n2,-n1-n2])
        for p1 in pos:
            for n1 in neg:
                if -(p1+n1) in occurrences:
                    if -(p1+n1) == p1 and occurrences[p1] < 2:
                        continue
                    elif -(p1+n1) == n1 and occurrences[n1] < 2:
                        continue

                    if tuple(sorted([n1,p1,-(p1+n1)])) not in result_tuple_set:
                        results.append([p1,n1,-p1-n1])

        return results


s = Solution()
# a =  [-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]
print(s.threeSum([1,1,-2]))


