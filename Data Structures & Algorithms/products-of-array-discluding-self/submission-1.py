class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix=1
        res=[1]*len(nums)
        n=len(nums)
        for i in range (n):
            res[i]=prefix
            prefix=prefix*nums[i]
        
        postfix=1
        for i in range(n-1,-1,-1):
            res[i]=res[i]*postfix
            postfix=postfix*nums[i]
        
        return res
