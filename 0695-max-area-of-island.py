class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # Maintain a max area var
        # Loop through grid
            # If 1, start BFS and count cells
            # Mark cells visited by marking 0

        def get_area(i,j):
            q = collections.deque()
            q.append((i,j))
            grid[i][j] = 0
            neighbors = [(-1,0), (1,0), (0,-1), (0,1)]
            area = 0
            while q:
                i,j = q.popleft()
                area += 1

                for x,y in neighbors:
                    if 0 <= x+i < len(grid) and 0 <= y+j < len(grid[0]) and grid[x+i][y+j] == 1:
                        grid[x+i][y+j] = 0  # mark as visited so that we don't add to queue multiple times
                        q.append((x+i, y+j))
            
            return area
        
        max_area = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    area = get_area(i,j)
                    max_area = max(max_area, area)
                    print("island area", area)

        
        
        
        return max_area