class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l, sett = 0, set()
        s = nums
        for r in range(len(nums)):
            if r - l > k:
                sett.remove(s[l])
                l += 1
            if s[r] in sett:
                return True
            else:
                sett.add(s[r])
        return False
