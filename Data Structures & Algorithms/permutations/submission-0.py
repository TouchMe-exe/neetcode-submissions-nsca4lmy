class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res=[]
        def dfs(i,arr,visited):

            if len(arr)==len(nums):
                res.append(arr[:])
                return 
 
            
            for i in range (len(nums)):
                if i not in visited:
                    arr.append(nums[i])
                    visited.add(i)
                    dfs(i,arr,visited)
                    arr.pop()
                    visited.remove(i)

        dfs(0,[],set())

        return res


