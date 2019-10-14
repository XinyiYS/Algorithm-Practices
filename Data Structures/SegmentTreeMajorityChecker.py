class SegmentTree:
    
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self._left = None
        self._right = None
        self.val = -sys.maxsize
    
    @property
    def mid(self):
        return (self.start + self.end) // 2
    
    @property
    def left(self):
        if not self._left:
            self._left = SegmentTree(self.start, self.mid)
        return self._left

    @property
    def right(self):
        if not self._right:
            self._right = SegmentTree(self.mid, self.end)
        return self._right
    
    def query(self, left, right, arr, positions):
        
        def is_majority(elem):
            l = bisect.bisect_left(positions[elem], left)
            r = bisect.bisect_right(positions[elem], right - 1)
            if 2 * (r - l) > right - left:
                return True
            return False
        
        if left >= right:
            return -1
        else:
            res = -1
            if left == self.start and right == self.end:
                if left == right - 1:
                    self.val = arr[left]
                elif self.val == -sys.maxsize:
                    elem1 = self.left.query(left, self.mid, arr, positions)
                    elem2 = self.right.query(self.mid, right, arr, positions)
                    if elem1 != -1 and is_majority(elem1):
                        self.val = elem1
                    elif elem2 != -1 and is_majority(elem2):
                        self.val = elem2
                    else:
                        self.val = -1
                res = self.val 
            else:
                elem1 = self.left.query(left, min(right, self.mid), arr, positions)
                elem2 = self.right.query(max(left, self.mid), right, arr, positions)
                if elem1 != -1 and is_majority(elem1):
                    res = elem1
                elif elem2 != -1 and is_majority(elem2):
                    res = elem2
            
            return res
            

class MajorityChecker:

    def __init__(self, arr: List[int]):
        self.arr = arr
        self.positions = collections.defaultdict(list)
        for i, n in enumerate(arr):
            self.positions[n].append(i)
        self.ST = SegmentTree(0, len(self.arr))
    
    def query(self, left: int, right: int, threshold: int) -> int:
        res = self.ST.query(left, right+1, self.arr, self.positions)
    
        l = bisect.bisect_left(self.positions[res], left)
        r = bisect.bisect_right(self.positions[res], right)
        
        return res if r - l >= threshold else -1