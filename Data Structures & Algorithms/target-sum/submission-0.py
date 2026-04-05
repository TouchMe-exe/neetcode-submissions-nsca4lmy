class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        mem={}
        def rec(total,i):

            if i==len(nums):
                if total == target:
                    return 1
                else:
                    return 0

            if (total,i) in mem:
                return mem[(total,i)]

            max_len = rec(total+nums[i],i+1) + rec(total-nums[i],i+1)
            mem[(total,i)] = max_len
            return max_len


        
        return rec(0,0)