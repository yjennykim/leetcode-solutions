class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counts_s1 = {}
        for ch in s1:
            counts_s1[ch] = counts_s1.get(ch, 0) + 1
        
        window = {}
        def is_included():
            for ch in counts_s1:
                if ch not in window:
                    return False
                
                if window[ch] < counts_s1[ch]:
                    return False

            return True
        
        l = 0
        for r in range(len(s2)):
            window[s2[r]] = window.get(s2[r], 0) + 1
            if is_included():
                return True

            if r-l+1 >= len(s1):
                window[s2[l]] -= 1
                l += 1

        return False

