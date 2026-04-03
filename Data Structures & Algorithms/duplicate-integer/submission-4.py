class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = {}

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        for count in count.values():
            if count != 1:
                return True
        return False