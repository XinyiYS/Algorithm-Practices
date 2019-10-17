# 1220. Count Vowels Permutation
# https://leetcode.com/problems/count-vowels-permutation/description/

# Given an integer n, your task is to count how many strings of length n can be formed under the following rules:

# Each character is a lower case vowel ('a', 'e', 'i', 'o', 'u')
# Each vowel 'a' may only be followed by an 'e'.
# Each vowel 'e' may only be followed by an 'a' or an 'i'.
# Each vowel 'i' may not be followed by another 'i'.
# Each vowel 'o' may only be followed by an 'i' or a 'u'.
# Each vowel 'u' may only be followed by an 'a'.
# Since the answer may be too large, return it modulo 10^9 + 7.



class Solution:
    def countVowelPermutation(self, n: int) -> int:
        if n == 1 : return 5
        a,e,i,o,u, const = 1,1,1,1,1, int(1e9+7)
        for iter in range(2, n+1):
        	a, e, i, o, u = (e+i+u)%const, (a+i)%const, (e+o)%const, (i)%const, (i+o)%const        	
        return (a+e+i+o+u) % const
s = Solution()
n = 100
a = s.countVowelPermutation(n)
print(a)