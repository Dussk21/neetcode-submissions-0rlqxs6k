class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n == 1 or n == 0:
            return nums

        m = n // 2
        L = nums[:m]
        R = nums[m:]

        L = self.sortArray(L)
        R = self.sortArray(R)

        sorted_arr = [0] * n
        l, r = 0, 0
        i = 0
        l_length = len(L)
        r_length = len(R)

        while l < l_length and r < r_length:
            if L[l] > R[r]:
                sorted_arr[i] = R[r]
                r += 1
            else:
                sorted_arr[i] = L[l]
                l += 1
            i += 1

        while l < l_length:
            sorted_arr[i] = L[l]
            l += 1
            i += 1

        while r < r_length:
            sorted_arr[i] = R[r]
            r+=1
            i += 1

        return sorted_arr