class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n == 0: return []
        if n == 1: return nums

        forward = [0] * n
        backward = [0] * n
        res = [1] * n

        running = 1
        for i in range(len(nums)):
            running *= nums[i]
            forward[i] = running

        running = 1 # reset
        for i in range(len(nums)-1, -1, -1):
            running *= nums[i]
            backward[i] = running
        
        for i in range(len(nums)):
            if i - 1 >= 0:
                res[i] *= forward[i-1]
            if i + 1 < len(nums):
                res[i] *= backward[i+1]
        
        return res