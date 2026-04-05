class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        
        def dfs(i:int,res:int)->int:
            if i>=len(nums):
                return res
            return dfs(i+1,res)+dfs(i+1,res^nums[i])
        
        return dfs(0,0)
