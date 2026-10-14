class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        land = 0
        shared = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    land += 1
                    
                    if i < rows-1 and grid[i+1][j] == 1:
                        shared += 1
                    if j < cols-1 and grid[i][j+1] == 1:
                        shared += 1
        return land * 4 - shared * 2