class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        mem = {}

        def rec(i, j, can_buy):

            if (i,j,can_buy) in mem:
                return mem[i,j,can_buy]

            if i >= len(prices):
                return 0
            
            if can_buy:
                res = max(rec(i+1, i, False), rec(i+1, j, True))
            
            else:
                res = max(prices[i] - prices[j] + rec(i+2, j, True), rec(i+1, j, False))
            
            mem[i,j,can_buy] = res
            return res
            
        
        return rec(0,0,True)

            
            