class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        def rec(i, j, can_buy):

            if i >= len(prices):
                return 0
            
            if can_buy:
                return max(rec(i+1, i, False), rec(i+1, j, True))
            
            else:
                return max(prices[i] - prices[j] + rec(i+2, j, True), rec(i+1, j, False))
            
        
        return rec(0,0,True)

            
            