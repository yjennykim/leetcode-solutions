class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        
        # store largest number in sequence and corresponding length
        store = set(nums)
        sequences = {}
        while len(store) > 0:
            first = store.pop()
            sequences[first] = sequences.get(first-1, 0) + 1

            temp = first
            while temp - 1 in store:
                store.remove(temp-1)
                sequences[first] += 1
                temp -= 1

        print(sequences)
        return max(sequences.values())
        
        
