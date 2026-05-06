class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)

        # 0, k-1
        # k, n-1

        def revv(arr, l, r):
            while l <= r:
                arr[l], arr[r] = arr[r], arr[l]
                l, r = l+1, r-1
        
        revv(nums, 0, len(nums)-1)
        revv(nums, 0, k-1)
        revv(nums, k, len(nums)-1)
                

            