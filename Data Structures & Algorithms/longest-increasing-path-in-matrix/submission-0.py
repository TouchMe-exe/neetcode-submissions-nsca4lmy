class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        n = len(matrix)-1
        m = len(matrix[0])-1
        max_len = 1
        mem={}

        def dfs(i,j, prev_val):

            if i>n or j>m or i<0 or j<0 or matrix[i][j] <= prev_val:
                return 0

            if (i,j) in mem:
                return mem[(i,j)]

            prev = matrix[i][j]
            res = 1 + max(dfs(i+1,j,prev),dfs(i,j+1,prev),dfs(i-1,j,prev),dfs(i,j-1,prev))

            mem[(i,j)] = res
            return res

        for i in range(n+1):
            for j in range(m+1):  
                max_len = max(max_len,dfs(i,j,-1))
        
        return max_len