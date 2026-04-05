class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l,total=0,0
        min_w=len(nums)
        
        for i in range(len(nums)):
            total+=nums[i]
            while total>=target:
                min_w=min(min_w,i-l+1)
                total-=nums[l]
                l+=1
        total=0
        for i in range (len(nums)):
            total+=nums[i]

        if total<target:
            return 0
        else:
            return min_w
        