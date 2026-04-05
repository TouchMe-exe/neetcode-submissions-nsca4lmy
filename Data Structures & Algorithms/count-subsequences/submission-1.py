class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        mem={}

        def rec(i,j):

            if j == len(t):
                return 1
            
            if i == len(s):
                return 0
            
            if (i,j) in mem:
                return mem[(i,j)]
            
            if s[i] == t[j]:
                count = rec(i+1,j+1) + rec(i+1,j)
            else:
                count = rec(i+1,j)

            mem[(i,j)] = count
            return count
        
        return rec(0,0)
            
            
        