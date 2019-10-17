# https://leetcode.com/problems/set-matrix-zeroes/description/
# Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.

class Solution:
    def setZeroes(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        N, M = len(matrix), len(matrix[0])
        firstRow = any([a==0 for a in matrix[0]])
        firstCol = any([matrix[i][0] == 0 for i in range(N)])

        for i in range(N):
        	for j in range(M):
        		if matrix[i][j] == 0:
        			matrix[0][j] = matrix[i][0] = 0
        for i in range(1, N):
        	for j in range(1, M):

        		if matrix[i][0] == 0 or matrix[0][j] == 0:
        			matrix[i][j] = 0

        if firstRow: 
        	for j in range(M):
        		matrix[0][j] = 0 
        if firstCol: 
        	for i in range(N):
        		matrix[i][0] = 0 

"""
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]"""
matrix = [[0,1,2,0],[3,4,5,2], [1,3,1,5]]
matrix = [[0],[1]]
s = Solution()
s.setZeroes(matrix)
print(matrix)