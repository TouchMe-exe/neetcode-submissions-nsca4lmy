class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        mem={}
        max_len = 0
        def rec(i, prev):
            
            if i == len(nums):
                return 0
            if (i, prev) in mem:
                return mem[(i,prev)]

            if nums[i] > prev:
                res = max(1 + rec(i+1, nums[i]) , rec(i+1, prev))
            else:
                res = rec(i+1, prev)
            
            mem[(i,prev)] = res
            return res

        return rec(0,-float('inf')) 