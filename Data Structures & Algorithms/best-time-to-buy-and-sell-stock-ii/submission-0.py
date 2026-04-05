class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i,j,profit=0,0,0
        while i < len(prices)-1:
            if prices[i]<prices[i+1]:
                profit+=(prices[i+1]-prices[i])
            i+=1
        return profit       
        

