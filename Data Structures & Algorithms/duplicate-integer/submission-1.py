class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        countNums = {}
        for i in range(len(nums)):
            countNums[nums[i]] = 1 + countNums.get(nums[i], 0)
        for count in countNums.values():
            if count != 1:
                return True
        return False
        # seen = set()
        # for num in nums:
        #     if num in seen:
        #         return True
        #     seen.add(num)
        # return False