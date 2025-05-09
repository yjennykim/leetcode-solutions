from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                # Minimum is in the right half
                l = mid + 1
            else:
                # Minimum is in the left half (including mid)
                r = mid
        return nums[l]
