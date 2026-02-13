class Solution:
    def sortedSquares(self, nums):
        output = [-1]*len(nums)
        l, r = 0, len(nums) - 1
        ptr = len(output) - 1
        while l <= r:
            if abs(nums[l]) >= abs(nums[r]):
                output[ptr] = nums[l]*nums[l]
                l += 1
            else:
                output[ptr] = nums[r]*nums[r]
                r -= 1
            ptr -= 1
        return output
