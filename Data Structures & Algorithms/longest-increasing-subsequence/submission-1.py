class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        def rec(i,res):

            if i>=len(nums):
                return 0

            count = 0

            if  len(res)==0 or res[-1]<nums[i]:
                res.append(nums[i])
                count = 1 + rec(i+1,res)
                res.pop()

            count = max(count,rec(i+1,res))
            
            return count
        
        return rec(0,[])
            
            
            
