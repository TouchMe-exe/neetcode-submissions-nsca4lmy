class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        arr=[]
        def dfs(i:int,currsum:int):

            if currsum>target:
                return
            if currsum==target:
                res.append(arr[:])
                return
            
            arr.append(nums[i])
            dfs(i,currsum+nums[i])
            arr.pop()
            
            if i+1<len(nums):
                dfs(i+1,currsum)
        
        dfs(0,0)
        return res
            
            
            

        