class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        def rec(l,r):
            if l > r:
                return 0
            final_result = 0
            for i in range (l,r+1):
                product = nums[i] * nums[l-1] * nums[r+1]
                result = product + rec(l,i-1) + rec(i+1, r)
                final_result = max(final_result, result)
            return final_result
        nums = [1] + nums + [1]
        return rec(1, len(nums)-2)