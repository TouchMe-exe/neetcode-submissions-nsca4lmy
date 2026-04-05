class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        def rec(i,j,res):

            if i == len(word1):
                return len(word2) - j
            
            if j == len(word2):
                return len(word1) - i
            
            if word1[i] == word2[j]:
                count = rec(i+1, j+1, res + word2[j])
            
            else:
                count = 1 + min(rec(i+1, j+1, res + word2[j]),
                                rec(i+1, j, res),
                                rec(i, j+1, res + word2[j])
                                )

            return count
        
        return rec(0,0,"")
