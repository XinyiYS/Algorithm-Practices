# https://leetcode.com/contest/weekly-contest-102/problems/fruit-into-baskets/

class Solution(object):
    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """

        res = 0
        i = 0

        while i < len(tree)-1:
            curr = 1
            j = i + 1

            type = 0
            another = -1
            curr_fruit = tree[i]
            while j < len(tree):
                next_fruit = tree[j]
                if next_fruit == curr_fruit or next_fruit == another:
                    curr += 1
                    j += 1
                elif next_fruit != curr_fruit and type == 0:
                    another = next_fruit
                    curr += 1
                    type = 1
                    first_different = j
                    j += 1
                else:
                    res = max(res , curr)
                    i = first_different
                    break



        return res

s = Solution()
a = [1,2,3,2,2]
# a= [3,3,3,1,2,1,1,2,3,3,4]
print(s.totalFruit(a))