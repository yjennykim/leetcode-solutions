class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # If touching 0 or out of bounds, then add to perimeter

        perimeter = 0
        queue = collections.deque()
        neighbors = [(-1,0), (1,0), (0,1), (0,-1)]

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # if land, look at neighboring cells
                if grid[i][j] == 1:
                    for x,y in neighbors:
                        # if out of bounds, then add to perimeter
                        if x+i < 0 or x+i >= len(grid) or y+j < 0 or y+j >= len(grid[0]) or grid[x+i][y+j] == 0:
                            perimeter += 1  
        
        return perimeter
