class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        mem={}
        def rec(i,j):
            
            res = 0
            if i==len(text1) or j==len(text2):
                return 0
            
            if (i,j) in mem:
                return mem[(i,j)]
            
            if text1[i] == text2[j]:
                res = 1 + rec(i+1, j+1)
            
            res = max(rec(i+1,j+1),rec(i,j+1),rec(i+1,j),res)
            
            mem[(i,j)] = res
            return res
        

        return rec(0,0)
        