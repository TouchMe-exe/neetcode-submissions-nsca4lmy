class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        mem={}
        def rec(r,c):

            if r>m-1 or c>n-1:
                return 0
            
            if (r==m-1 and c==n-1):
                return 1
            
            if (r,c) in mem:
                return mem[(r,c)]

            path = 0
            path = rec(r+1,c) + rec(r,c+1)

            mem[(r,c)] = path
            return path
        
        return rec(0,0)
            
        