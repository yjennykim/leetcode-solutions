class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        countBoats = l = 0
        r = len(people) - 1

        while l <= r:
            if people[r] > limit:
                return -1

            combinedWeight = people[l] + people[r]
            if combinedWeight > limit:
                r -= 1
            else:
                l += 1
                r -= 1    
            countBoats += 1

        return countBoats
