class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        flag = 0
        for i in range(1, len(nums)):
            if nums[i-1] > nums[i]: # decreasing
                if flag > 0:
                    return False

                if i == 1 or i == len(nums)-1: # simply update to really small number or really big number
                    flag += 1
                    continue
                
                print(f"nums[i-2]={nums[i-2]}, nums[r+1]={nums[i+1]}")
                if not (nums[i-2] <= nums[i-1] <= nums[i+1]): # left is incorrect
                    nums[i-1] = nums[i-2]
                    flag += 1
                
                if not (nums[i-2] <= nums[i-1] <= nums[i] <= nums[i+1]): # right is incorrect
                    nums[i] = nums[i+1]
                    flag += 1      

        return flag <= 1