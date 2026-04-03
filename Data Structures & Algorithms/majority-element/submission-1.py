class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res, maxC = 0, 0
        cnt = {}

        for n in nums:
            cnt[n] = 1 + cnt.get(n, 0)
            res = n if cnt[n] > maxC else res
            maxC = max(maxC, cnt[n])
        return res