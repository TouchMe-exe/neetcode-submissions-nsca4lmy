class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res=set()
        
        def dfs(i,arr,visited):

            if len(arr)==len(nums):
                res.add(tuple(arr))
                return 
            
            for j in range (len(nums)):
                
                if (j,nums[j]) not in visited:
                    arr.append(nums[j])
                    visited.add((j,nums[j]))
                    dfs(j,arr,visited)
                    arr.pop()
                    visited.remove((j,nums[j]))

        dfs(0,[],set())

        return list(res)