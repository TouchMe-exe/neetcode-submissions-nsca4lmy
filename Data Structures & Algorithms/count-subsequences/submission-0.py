class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        mem={}

        def rec(i,res):

            if res == t:
                return 1
            
            if i == len(s):
                return 0
            
            if (i,res) in mem:
                return mem[(i,res)]

            count = rec(i+1,res+s[i]) + rec(i+1,res)
            mem[(i,res)] = count
            return count
        
        return rec(0,"")
            
            
        