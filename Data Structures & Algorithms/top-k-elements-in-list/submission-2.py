class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countNums = {}
        res = []

        for i in range(len(nums)):
            countNums[nums[i]] = countNums.get(nums[i], 0) + 1
        
        sortedCount = sorted(countNums, key= lambda x: countNums[x], reverse = True)

        for i in range(k):
            res.append(sortedCount[i])

        return res