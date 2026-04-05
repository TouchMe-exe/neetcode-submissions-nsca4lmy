class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        mem={}

        def dfs(index, sol):

            if index == len(nums):
                return sol

            if (index, sol) in mem:
                return mem[(index,sol)]

            sol = max(dfs(index+1, sol*nums[index]), dfs(index+1, nums[index]), sol)
            mem[(index,sol)] = sol

            return mem[(index,sol)]

        
        return dfs(1,nums[0])