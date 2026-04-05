class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        mem={}

        def rec(i,total):

            if total > amount:
                return 0
            
            if total == amount:
                return 1

            if (i,total) in mem:
                return mem[(i,total)]

            count = 0
            for index in range(i,len(coins)):
                count += rec(index, total + coins[index]) 
            
            mem[(i,total)] = count
            return count
        
        return rec(0,0)

            

