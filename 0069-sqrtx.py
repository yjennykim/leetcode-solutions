class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2: return x

        low, high = 2, x // 2 
        
        while low <= high:
            mid = (low + high) // 2
            exp = mid * mid
            if exp > x:
                # too high
                high = mid - 1
            elif exp < x:
                # too low
                low = mid + 1
            else:
                return mid
        
        return high
            