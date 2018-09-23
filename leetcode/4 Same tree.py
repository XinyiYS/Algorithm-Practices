# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """

        def compare(p, q):
            if p is None and q is None:
                return True
            elif (p is None and q is not None) or (p is not None and q is None):
                return False
            else:
                return (p.val == q.val) and (compare(p.left, q.left) and compare(p.right, q.right))

        return compare(p, q)




