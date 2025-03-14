class Solution:
    def maxArea(self, height: List[int]) -> int:
        # create two pointers
        p1, p2 = 0, len(height)-1

        # keep track of maximum water
        maxWater = 0

        # while not overlapping
        while p1 <= p2:
            base = p2 - p1
            currHeight = min(height[p1], height[p2])
            maxWater = max(maxWater, base * currHeight) # calculate the area, set max value
            if height[p1] < height[p2]:
                p1 += 1
            else:
                p2 -= 1

        # return max water
        return maxWater
