class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l, r = max(nums), sum(nums)
        res = r

        def canSum(largest):
            subArrays, currSum = 0, 0
            for n in nums:
                currSum += n
                if currSum > largest:
                    subArrays += 1
                    currSum = n
            return subArrays + 1 <= k
            
        while l <= r:
            mid = l + (r-l) // 2
            if canSum(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res