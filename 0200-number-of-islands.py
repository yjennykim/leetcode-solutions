import collections
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        neighbors = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        self.islands = 0
        def bfs(i,j):
            q = collections.deque()
            q.append([i, j])

            while len(q) > 0:
                curr_i, curr_j = q.popleft()
                
                for x, y in neighbors:
                    new_x, new_y = curr_i + x, curr_j + y

                    # if in bounds
                    if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]) and grid[new_x][new_y] == "1":
                        q.append((new_x, new_y))
                        grid[new_x][new_y] = "0"

            self.islands += 1

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    bfs(i,j)

        return self.islands

                
            
            

