class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        
        def recurse(arr):

            if len(arr) == 1:
                return arr[0]

            final_result = 0

            for i in range (len(arr)):
                product = arr[i]

                if i-1>=0:
                    product = product * arr[i-1]
                if i+1<=len(arr)-1:
                    product = product * arr[i+1]
                
                copy=arr[:]
                del copy[i]
                result = product + recurse(copy)

                final_result = max(final_result,result)
            
            return final_result
        
        return recurse(nums)

                
                


            

