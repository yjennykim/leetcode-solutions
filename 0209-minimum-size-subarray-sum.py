class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_length = math.inf
        window_sum = 0
        l = 0

        for r in range(len(nums)):
            window_sum += nums[r]

            while window_sum >= target:
                min_length = min(min_length, r-l+1)

                # shrink the window
                window_sum -= nums[l]
                l += 1
        
        return min_length if min_length != math.inf else 0