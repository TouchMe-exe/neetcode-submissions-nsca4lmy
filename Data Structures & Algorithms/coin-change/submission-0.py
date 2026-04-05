class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        mem={}
        def rec(num_coin,curr_amt):
            if curr_amt==amount:
                return num_coin
            if curr_amt>amount:
                return float('inf')
            
            if (num_coin,curr_amt) in mem:
                return mem[(num_coin,curr_amt)]

            min_coin = float('inf')
            for c in coins:
                branch = rec(num_coin+1,curr_amt+c)
                if branch != -1:
                    min_coin=min(min_coin,branch)

            mem[(num_coin,curr_amt)] = min_coin

            if min_coin == float('inf'):
                return -1
            else:
                return min_coin

        return rec(0,0)