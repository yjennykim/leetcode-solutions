class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        target_freq = len(nums) // 3

        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        res = []
        for k,v in count.items():
            if v > target_freq:
                res.append(k)
        
        return res