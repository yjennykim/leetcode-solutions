class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1, max(piles)

        while l <= r:
            k = (l + r) // 2
            print(f"trying k={k}")
            
            time = 0
            for pile in piles:
                time += math.ceil(pile / k)
            print(f"time={time}")
            if time <= h: # we have more time
                r = k - 1   # try eating less bananas
            else:
                l = k + 1
        
        return l