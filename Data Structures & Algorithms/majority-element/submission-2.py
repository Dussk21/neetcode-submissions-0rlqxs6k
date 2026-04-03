class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res, count = 0, 0

        for n in nums:
            if count == 0:
                res = n
            
            count += (1 if n == res else -1)

            # if n == res:
            #     count += 1
            # else:
            #     count -= 1

        return res
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # res, maxC = 0, 0
        # cnt = {}

        # for n in nums:
        #     cnt[n] = 1 + cnt.get(n, 0)
        #     res = n if cnt[n] > maxC else res
        #     maxC = max(maxC, cnt[n])
        # return res