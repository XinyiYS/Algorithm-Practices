class Node:
    def __init__(self, start, end, sum, left, right):
        self.start = start
        self.end = end 
        self.sum = sum
        self.left = left
        self.right = right

class SegmentTree:
    def __init__(self, nums):
        if not nums:return 
        self.root = self.buildTree(0,len(nums)-1, nums)
    
    def buildTree(self, start, end, nums):
        if start==end:
            return Node(start, end, nums[start], None, None)
        
        mid = (start+end)//2
        left = self.buildTree(start, mid, nums)
        right = self.buildTree(mid+1, end, nums)
        return Node(start, end,left.sum+right.sum, left, right)
    
    def update(self, node, index, value):        
        if index == node.start == node.end:
            node.sum = value
            return
        
        mid = (node.start + node.end) // 2
        if index <= mid:
            self.update(node.left, index, value)
        else:
            self.update(node.right, index, value)
        node.sum = node.left.sum + node.right.sum
        return
    
    def sumRange(self, root, i, j):
        
        if root.start == i and j == root.end:
            return root.sum
        
        mid = (root.start+root.end)//2
        if j <= mid:
            return self.sumRange(root.left, i, j)
        elif i > mid:
            return self.sumRange(root.right, i, j)
        else:
            return self.sumRange(root.left, i, mid) + self.sumRange(root.right, mid+1, j)
        
class NumArray:

    def __init__(self, nums: List[int]):
        self.ST = SegmentTree(nums)
        
        
    def update(self, i: int, val: int) -> None:
        self.ST.update(self.ST.root, i, val)


    def sumRange(self, i: int, j: int) -> int:
        return self.ST.sumRange(self.ST.root, i, j)
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)