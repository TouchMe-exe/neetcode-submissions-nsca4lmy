class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res=[]
        
        def dfs(i,arr,visited):

            if len(arr)==len(nums):
                res.append(arr[:])
                return 

            if i==len(nums):
                return

            for j in range(len(nums)):
                if j not in visited:
                    
                    arr.append(nums[j])
                    visited.add(j)
                    dfs(j,arr,visited)
                    arr.pop()
                    visited.remove(j)
        
        dfs(0,[],set())

        return res


