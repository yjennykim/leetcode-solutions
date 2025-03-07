import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for num in nums:
            counter[num] = counter.get(num, 0) + 1
        
        # sort by value
        counterAsList = []
        for num, count in counter.items():
            heapq.heappush(counterAsList, (count, num))

        print(counterAsList)
        largestKItems = heapq.nlargest(k, counterAsList)
        
        res = []
        for count, num in largestKItems:
            res.append(num)

        return res
        


