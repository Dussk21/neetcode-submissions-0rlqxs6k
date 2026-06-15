class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        def find_peek(arr):
            l, r = 0, arr.length()-1
            while l < r:
                m = l + (r-l) // 2
                if arr.get(m) < arr.get(m+1):
                    l = m + 1
                else:
                    r = m
            return l
        peek = find_peek(mountainArr)
        def find_left(arr, targ):
            l, r = 0, peek
            val = -1
                
            while l <= r:
                m = l + (r-l) // 2
                if arr.get(m) == targ:
                    val = m
                    r = m - 1
                elif arr.get(m) < targ:
                    l = m + 1
                else:
                    r = m - 1
            return val
        
        def find_right(arr, targ):
            l, r = peek, arr.length()-1
            val = -1 
            while l <= r:
                m = l + (r-l) // 2
                if arr.get(m) == targ:
                    val = m
                    l = m + 1
                elif arr.get(m) > targ:
                    l = m + 1
                else:
                    r = m - 1
            return val
        

        left = find_left(mountainArr, target)
        if left != -1:
            return left
        right = find_right(mountainArr, target)
        return right
