# 986. Interval List Intersections
# https://leetcode.com/problems/interval-list-intersections/description/


class Solution:
    def intervalIntersection(self, A, B):
        # for any two intervals, their intersection = [max(begin1,begin2), min(end1,end2)], if overlap
        i = j = 0
        res = []
        while i < len(A) and j < len(B):
            a, b = A[i], B[j]
            compare = self.check(a, b)
            if compare == 1:  # A[i] is later than B[j], i.e. B[j] is no longer possible for an intersection
                j += 1
            elif compare == -1:
                i += 1
            else:
                res.append(self.getIntersection(a, b))
                i += int(a[1] <= b[1])
                j += int(a[1] >= b[1])
        
        return res
    
    def check(self, int1, int2):
        # returns 1, -1, 0
        # 1 means int1 > int2 , no intersection, e.g. [10, 12] and [3, 9]
        # 0 means there is overlap
        # -1 means int1 < int2, no intersection [4, 8] and [9, 11]
        if int1[0] > int2[1]: return 1
        elif int2[0] > int1[1]: return -1
        else: return 0
        
    
    def getIntersection(self, int1, int2):
        return [max(int1[0], int2[0]), min(int1[1], int2[1])] 

s = Solution()
A = [[1,10],[100,101]]
B = [[1,2],[4,11]]
res = s.intervalIntersection(A, B)
print(res)




