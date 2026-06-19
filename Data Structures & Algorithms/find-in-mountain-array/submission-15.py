class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        def find_peek(arr):
            l, r = 0, arr.length() - 1
            pk = r
            while l < r:
                m = l + ((r-l) // 2)
                if arr.get(m) > arr.get(m+1):
                    pk = m
                    r = m - 1
                else:
                    l = m + 1
            return pk
        peek = find_peek(mountainArr)
        
        def search_left(pk, arr):
            l, r = 0, pk
            res = -1
            while l <= r:
                m = l + (r-l) // 2
                if arr.get(m) == target:
                    return m
                elif arr.get(m) > target:
                    r = m - 1
                else:
                    l = m + 1
            return res

        def search_right(pk, arr):
            l, r = pk+1, arr.length()-1
            res = -1
            while l <= r:
                m = l + (r-l) // 2
                if arr.get(m) == target:
                    return m
                elif arr.get(m) < target:
                    r = m - 1
                else:
                    l = m + 1
            return res
        
        left = search_left(peek, mountainArr)
        right = search_right(peek, mountainArr)
        if left != -1:
            return left
        else:
            return right
                