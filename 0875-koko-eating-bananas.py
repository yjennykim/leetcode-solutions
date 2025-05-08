class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def is_possible(k):
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / k)

            print(f"Is possible? k={k}, hours={hours}, {hours <= h}")
            return hours <= h
        
        l,r = 1,max(piles)
        while l <= r:
            m = (l+r) // 2
            possible = is_possible(m)
            if possible:
                # try eating less per hour
                r = m - 1
            else:
                l = m + 1
        
        return l
