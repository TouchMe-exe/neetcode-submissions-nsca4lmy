class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        arr=[]
        def dfs(i, currsum):

            if currsum == target:
                res.append(arr[:])
                return

            if currsum > target or i == len(nums):
                return
            
            arr.append(nums[i])
            dfs(i, currsum + nums[i])
            arr.pop()
            dfs(i+1, currsum)
            
        
        dfs(0,0)
        return res
            
            
            

        