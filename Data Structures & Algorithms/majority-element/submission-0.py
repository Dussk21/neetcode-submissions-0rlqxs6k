class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        countNums = {}

        for n in nums:
            countNums[n] = 1 + countNums.get(n, 0)

        sortedCount = sorted(countNums, key= lambda x: countNums[x], reverse=True)

        return sortedCount[0]