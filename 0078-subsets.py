class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        combos = []

        def generate_combos(i, curr_combos):
            if i >= len(nums):
                combos.append(curr_combos.copy())
                return

            
            curr_combos.append(nums[i])
            generate_combos(i+1, curr_combos)
            curr_combos.pop()
            generate_combos(i+1, curr_combos)
        
        generate_combos(0, [])
        return combos