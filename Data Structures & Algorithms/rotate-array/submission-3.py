class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        l,r  = 0, len(nums)-1
        # 0, k-1
        # k, n-1

        def revv(l, r):
            while l <= r:
                nums[l], nums[r] = nums[r], nums[l]
                l, r = l+1, r-1
        
        revv(0, len(nums)-1)
        revv(0, k-1)
        revv(k, len(nums)-1)
                

            