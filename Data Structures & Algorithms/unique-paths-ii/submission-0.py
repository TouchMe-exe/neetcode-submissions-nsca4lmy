class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        m = len(obstacleGrid) - 1
        n = len(obstacleGrid[0]) - 1
        mem={}

        def rec(r,c):

            if r > m or c > n:
                return 0

            if obstacleGrid[r][c] == 1:
                return 0
            
            if r == m and c == n:
                return 1
            
            if (r,c) in mem:
                return mem[(r,c)]

            path = rec(r,c+1) + rec(r+1,c)

            mem[(r,c)] = path
            return path

        return rec(0,0) 
        