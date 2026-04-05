class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        mem={}
        def rec(i,j):

            if i==len(text1) or j==len(text2):
                return 0
            
            if (i,j) in mem:
                return mem[(i,j)]

            
            if text1[i] == text2[j]:
                max_len = 1 + rec(i+1,j+1)
            
            else:    
                max_len = max(rec(i+1,j),rec(i,j+1))
            
            mem[(i,j)] = max_len
            return max_len
        

        return rec(0,0)
        