class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        has_violation = False
        for i in range(1, len(nums)):
            if nums[i-1] > nums[i]:
                if has_violation:
                    return False

                has_violation = True

                # Case 1: Nums[i-1] needs to be higher
                if i == 1 or nums[i-2] <= nums[i]:
                    nums[i-1] = nums[i]

                # Case 2: Nums[i] needs to be lowere
                else:
                    nums[i] = nums[i-1]
                
        return True
            
