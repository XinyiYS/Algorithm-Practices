# https://leetcode.com/problems/path-sum-iii/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """

        def solve(node, sum, partial_sum):
            if node is None:
                return 0

            recurse_result = solve(node.left, sum, sum) + solve(node.right, sum, sum)

            if node.val == sum:
                return recurse_result + 1

            if node.val == partial_sum:
                return recurse_result + 1
            else:
                return solve(node.left, sum, partial_sum - node.val) + solve(node.right, sum,
                                                                             partial_sum - node.val) + recurse_result

        return solve(root, sum, sum)

