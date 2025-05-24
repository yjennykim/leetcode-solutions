from typing import List

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        sequence = {char: i for i, char in enumerate(order)}

        for i in range(1, len(words)):
            prev = words[i - 1]
            curr = words[i]
            found_diff = False

            for j in range(min(len(prev), len(curr))):
                if sequence[curr[j]] < sequence[prev[j]]:
                    return False
                elif sequence[curr[j]] > sequence[prev[j]]:
                    found_diff = True
                    break  # correct order, no need to compare further
            
            if not found_diff and len(curr) < len(prev):
                return False  # curr is a prefix of prev

        return True
