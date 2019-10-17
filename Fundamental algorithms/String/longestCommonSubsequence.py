import string
import random

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        #dp[i][j] represents the max length of common subsequence starting up to text1[i] and text2[j]
        
        # if text1[i] == text2[j] : dp[i+1][j+1] = 1 + dp[i][j]
        # else:dp[i+1][j+1] = max(dp[i-1][j], dp[i][j-1])
        # return dp[-1][-1]
        
        dp  = [ [0 for i in range(len(text2))] for j in range(len(text1))]
        dp[0][0] = int(text1[0] == text2[0])
        for i in range(1,len(text1)):
            dp[i][0] = max(dp[i-1][0], int(text1[i]==text2[0]))
        for j in range(1,len(text2)):
            dp[0][j] = max(dp[0][j-1], int(text1[0]==text2[j]))
        
        # [print(row) for row in dp]
        
        for i in range(1, len(text1)):
            for j in range(1, len(text2)):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        # [print(row) for row in dp]
        return dp[-1][-1]


def random_generator(size=6, chars=string.ascii_lowercase[:10]):
    return ''.join(random.choice(chars) for x in range(size))
a = random_generator(999)
b = random_generator(998)


# print("\""+a+"\"")
# print("\""+b+"\"")
s = Solution()
# a = "hofbmnyr"
# b = "phdofcmr"
length = s.longestCommonSubsequence(a,b)
print(length)
