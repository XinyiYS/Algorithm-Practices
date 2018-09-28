# https://leetcode.com/problems/basic-calculator/description/


class Solution:
    def calculate(self, s):
        total = 0
        i, signs = 0, [1, 1]
        while i < len(s):
            c = s[i]
            if c.isdigit():
                # beginning of a number, such as the index of '2' in '23'
                start = i
                while i < len(s) and s[i].isdigit():
                    i += 1
                total += signs.pop() * int(s[start:i])
                continue
            if c in '+-(':
                # append to the end of the signs stack
                signs += signs[-1] * (1, -1)[c == '-'],
            elif c == ')':
                signs.pop()
            i += 1
        return total
