class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        if sum(nums)%2 != 0:
            return False
        else:
            target = sum(nums)/2

        mem={}
        def rec(i, curr_sum):

            if curr_sum == target:
                return True
            
            if i == len(nums):
                return False
            
            if (i,curr_sum) in mem:
                return mem[(i,curr_sum)]

            mem[(i,curr_sum)] = rec(i+1, curr_sum + nums[i]) or rec(i+1, curr_sum)

            return mem[(i,curr_sum)]
        
        return rec(0,0)
            
        