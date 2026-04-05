class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        mem = {}

        def dfs(i,j):

            if i<0 or i >= len(grid) or j<0 or j >= len(grid[0]):
                return float('inf')
            
            if i == len(grid)-1 and j == len(grid[0])-1:
                return grid[i][j]
            
            if (i, j) in mem:
                return mem[(i, j)] 

            result = grid[i][j] + min(dfs(i+1, j), dfs(i, j+1))
            mem[(i,j)] = result
            
            return result
        
        return dfs(0,0)
                                        
            
