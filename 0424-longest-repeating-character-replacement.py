class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = {}
        longest_substr = 0
        l, r = 0, 0
        while r < len(s):
            if s[r] not in counter:
                counter[s[r]] = 0
            counter[s[r]] += 1
            
            subs = (r-l+1) - max(counter.values())  # number of substitutions needed = window size - most common value

            # start removing from left window
            while subs > k:
                counter[s[l]] -= 1
                # if counter[s[l]] == 0:
                #     del counter[s[l]]
                l += 1
                subs = (r-l+1) - max(counter.values())
            
            longest_substr = max(longest_substr, r-l+1)
            r += 1

        return longest_substr
            

 