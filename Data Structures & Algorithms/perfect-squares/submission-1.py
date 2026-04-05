class Solution:
    def numSquares(self, n: int) -> int:
        i = 1
        square_nums = []
        mem = {}

        while i*i <= n:
            square_nums.append(i*i)
            i += 1
        
        def rec(i, num):
            if num == n:
                return 0
            
            if i > len(square_nums) - 1 or num > n:
                return float('inf')
            
            if (i, num) in mem:
                return mem[(i,num)]

            res = min(1 + rec(i+1, num + square_nums[i]), 
            rec(i+1, num), 
            1 + rec(i, num + square_nums[i])
            )

            mem[(i,num)] = res
            return res
        
        return rec(0,0)
            
            
            
