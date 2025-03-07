import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for num in nums:
            counter[num] = counter.get(num, 0) + 1
        
        return [num for num, count in heapq.nlargest(k, counter.items(), key=lambda x: x[1])]
        


