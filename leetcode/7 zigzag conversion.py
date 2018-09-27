# https://leetcode.com/problems/zigzag-conversion/description/

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s

        result =''
        #1st row
        i = 0
        while(i<len(s)):
            result += s[i]
            i += (numRows*2-2)

        #2nd to second last row
        for i in range(1, numRows-1):
            j = i
            while(  j < len(s)):
                result += s[j]
                if j + numRows*2-2-i-i < len(s):
                    result += s[j + numRows * 2 - 2 - i-i]
                j += numRows*2-2

        #last row
        i = numRows - 1
        while(i < len(s)):
            result += s[i]
            i += numRows*2 -2

        return result

s= Solution()
a = s.convert("ABCD", 3)

print(a)
print("ABDC")