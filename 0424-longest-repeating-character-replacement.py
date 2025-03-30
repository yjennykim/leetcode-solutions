class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        counts = {}
        longest = 0

        def is_valid():
            most_counted_character = max(counts, key=counts.get)

            replace_count = 0
            for ch, count in counts.items():
                if ch != most_counted_character:
                    replace_count += count
            
            return True if replace_count <= k else False
        
        for r in range(len(s)):
            counts[s[r]] = counts.get(s[r], 0) + 1

            while not is_valid():
                counts[s[l]] -= 1
                l += 1

            longest = max(longest, r-l+1)

        return longest