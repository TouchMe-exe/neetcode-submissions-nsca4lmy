class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2:
                return 1
        if n == 3:
                return 2

        mem={}
        def rec(num):
            
            if num == 0:
                return 1
            if num in mem:
                return mem[num]

            final_product = 1

            for i in range(1,num+1):
                product = i * rec(num-i)
                final_product=max(final_product,product)

            mem[num]=final_product
            return final_product
        
        return rec(n)

