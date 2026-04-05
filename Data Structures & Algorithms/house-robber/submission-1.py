class Solution:
    def rob(self, nums: List[int]) -> int:
        mem={}
        def rob(n):
            if n>=len(nums):
                return 0
            if n in mem:
                return mem[n]
            mem[n]=max(nums[n]+rob(n+2),rob(n+1))    
            return mem[n]
            
        return rob(0)
        