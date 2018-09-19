# https://leetcode.com/problems/score-of-parentheses/description/
class Solution(object):
    def scoreOfParentheses(self, S):

        """
        :type S: str
        :rtype: int
        """
        score = 0
        i = 0
        stack = []
        status = False
        while i < len(S):
            if S[i] == '(':
                stack.append('(')
                status =True
            else:
                stack.pop(-1)
                if status:
                    score += 2 ** len(stack)
                    status =False
            i+=1

        return score









