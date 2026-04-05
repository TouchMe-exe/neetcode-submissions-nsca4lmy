class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, total = 0, 0
        min_w = float("inf")
        
        for r in range(len(nums)):
            total += nums[r]
            while total >= target:
                min_w = min(min_w, r-l+1)
                total -= nums[l]
                l += 1
 
        return min_w if min_w != float("inf") else 0
        