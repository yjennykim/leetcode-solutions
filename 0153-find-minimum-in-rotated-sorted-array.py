class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        # [4,5,6,7,0,1,2]
        smallest = nums[0]

        while l <= r:
            m = (l + r) // 2
            smallest = min(nums[m], smallest)

            if nums[m] <= nums[r]:
                # nums[m] in the correct sorted list, search the left side
                r = m - 1
            else:
                l = m + 1
        
        return smallest