class Solution:
    def stoneGame(self, piles: List[int]) -> bool:

        i = 0
        j = len(piles)-1
        alice , bob = 0,0
        turn = 0

        mem = {}
        def rec(i,j,turn):
            if i >= j:
                return 0

            if (i,j,turn) in mem:
                return mem[(i,j,turn)]

            if turn % 2 == 0:
                res = max(piles[i]+rec(i+1,j,turn+1), piles[j]+rec(i,j-1,turn+1))
            
            else:
                res = max(rec(i+1,j,turn+1)-piles[i], rec(i,j-1,turn+1)-piles[j])
            
            mem[(i,j,turn)] = res
            return res
        
        if rec(0,len(piles)-1,0):
            return True
        else:
            return False
            