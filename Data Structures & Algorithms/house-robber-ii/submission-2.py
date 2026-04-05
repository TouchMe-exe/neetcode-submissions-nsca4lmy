class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        mem={}
        def recurse(l,r):

            if l>r:
                return 0
            if (l,r) in mem:
                return mem[(l,r)]  
            mem[(l,r)] = max(nums[l]+recurse(l+2,r),
            recurse(l+1,r))
            return mem[(l,r)]

        n = len(nums)-1
        return max(recurse(0,n-1),recurse(1,n))


        