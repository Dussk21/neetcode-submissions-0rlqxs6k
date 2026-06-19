class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        def find_peek(arr):
            l, r = 0, arr.length() - 1
            while l < r:
                m = l + (r-l) // 2
                if arr.get(m) > arr.get(m+1):
                    r = m
                else:
                    l = m + 1
            return l

        peek = find_peek(mountainArr)
        
        def search_left(pk, arr):
            l, r = 0, pk
            while l <= r:
                m = l + (r-l) // 2
                if arr.get(m) == target:
                    return m
                elif arr.get(m) > target:
                    r = m - 1
                else:
                    l = m + 1
            return -1

        def search_right(pk, arr):
            l, r = pk+1, arr.length()-1
            while l <= r:
                m = l + (r-l) // 2
                if arr.get(m) == target:
                    return m
                elif arr.get(m) < target:
                    r = m - 1
                else:
                    l = m + 1
            return -1
        
        left = search_left(peek, mountainArr)
        # right = search_right(peek, mountainArr)
        if left != -1:
            return left
        else:
            return search_right(peek, mountainArr)
                