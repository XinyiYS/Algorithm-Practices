# https://leetcode.com/problems/min-stack/description/

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minStack = []


    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if len(self.minStack) == 0 or x <= self.minStack[-1]:
            self.minStack.append(x)
        self.stack.append(x)
        return

    def pop(self):
        """
        :rtype: void
        """
        if len(self.stack) == 0:
            return

        if len(self.minStack) >= 1 and self.stack[-1] == self.minStack[-1]:
            self.minStack.pop()
        self.stack.pop()
        return

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1] if len(self.stack) > 0 else None

    def getMin(self):
        """
        :rtype: int
        """
        return self.minStack[-1] if len(self.minStack) > 0 else None
