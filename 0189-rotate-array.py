class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n  
        numSize = n
        start = 0

        while numSize > 0:
            current = start
            prevNum = nums[start]
            
            while True:
                newIndex = (current + k) % n
                nums[newIndex], prevNum = prevNum, nums[newIndex]
                current = newIndex
                numSize -= 1
                
                if current == start:
                    break
            
            start += 1