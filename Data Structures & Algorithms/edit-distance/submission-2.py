class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        mem={}
        def rec(i,j):

            if (i,j) in mem:
                return mem[(i,j)]

            if i == len(word1):
                return len(word2) - j
            
            if j == len(word2):
                return len(word1) - i
            

            if word1[i] == word2[j]:
                count = rec(i+1, j+1)
            
            else:
                count = 1 + min(rec(i+1, j+1),
                                rec(i+1, j),
                                rec(i, j+1)
                                )
            mem[(i,j)] = count
            return count
        
        return rec(0,0)
