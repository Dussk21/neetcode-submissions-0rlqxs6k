class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l, r = max(nums), sum(nums)
        res = r

        def canSum(largest):
            subArrs, curSum = 1, 0
            for n in nums:
                curSum += n
                if curSum > largest:
                    subArrs += 1
                    curSum = n
            return subArrs <= k
            
        while l <= r:
            m = l + (r-l) // 2
            if canSum(m):
                res = m
                r = m - 1
            else:
                l = m + 1


        return res