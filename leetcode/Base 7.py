# https://leetcode.com/problems/base-7/description/

class Solution:
    def convertToBase7(self, num: int) -> str:
    	if not num: return num
    	sign = 1 if num > 0 else -1
    	num, res = abs(num), ""
    	while num:
    		res = str(num % 7 ) +  res
    		num = num // 7 
    	return res if sign >0 else '-' + res

s = Solution()
a = s.convertToBase7(98)
print(a)