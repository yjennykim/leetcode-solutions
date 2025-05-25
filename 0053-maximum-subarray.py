class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Track largest sum: 0
        # For loop on nums --> i 
            # If running_total + nums[i] < 0:
                # Start new window
            
            # Add nums[i]
            # Override largest sum if needed
        
        # Return largest sum

        if len(nums) == 0:
            return 0

        largest_sum = nums[0]
        running_total = 0
        for r in range(len(nums)):
            running_total = max(running_total + nums[r], nums[r])
            largest_sum = max(running_total, largest_sum)
        
        return largest_sum