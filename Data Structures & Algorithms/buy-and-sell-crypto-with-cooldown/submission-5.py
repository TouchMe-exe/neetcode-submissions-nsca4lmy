class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        mem = {}

        def rec(i, can_buy):

            if (i,can_buy) in mem:
                return mem[(i,can_buy)]

            if i >= len(prices):
                return 0

            if can_buy:
                res = max(rec(i+1, not can_buy) - prices[i], rec(i+1, can_buy))
            else:
                res = max(rec(i+2, not can_buy) + prices[i], rec(i+1, can_buy))
            
            mem[(i,can_buy)] = res
            return res
            
        
        return rec(0, True)

            
            