class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1
        area = 0

        while l < r:
            new_area = min(heights[l], heights[r]) * (r - l)
            if new_area > area:
                area = new_area
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        
        return area