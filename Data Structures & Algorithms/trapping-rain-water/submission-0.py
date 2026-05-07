class Solution:
    def trap(self, height: List[int]) -> int:
        maxL, maxR = height[0], height[-1]
        l, r = 1, len(height)-2
        res = 0

        while l <= r:
            if maxL <= maxR:
                if height[l] < maxL:
                    res += maxL - height[l]
                else:
                    maxL = height[l]
                l += 1
            else:
                if height[r] < maxR:
                    res += maxR - height[r] 
                else:
                    maxR = height[r]
                r -= 1

        return res