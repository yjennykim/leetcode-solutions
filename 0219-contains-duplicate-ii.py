class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        l = 0

        for r in range(len(nums)):
            # if window is too big, shrink
            if r - l > k:
                window.remove(nums[l])
                l += 1
            
            # if duplicate exists in this window, then return True
            if nums[r] in window:
                return True
                
            window.add(nums[r])
        
        return False