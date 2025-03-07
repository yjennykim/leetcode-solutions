class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping = {} # define mapping of character in s -> character in t
        mapped = set()

        # loop through s
        for i in range(len(s)):
            if s[i] in mapping: # if character is in mapping
                if t[i] != mapping[s[i]]: # if character in t != mapped character: return false
                    return False
            elif t[i] in mapped:
                return False
            else:
                mapping[s[i]] = t[i]  # add to mapping
                mapped.add(t[i])

        return True