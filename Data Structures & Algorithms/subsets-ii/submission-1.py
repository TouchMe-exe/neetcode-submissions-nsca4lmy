class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=set()


        def dfs(i,arr):

            if i==len(nums):
                res.add(tuple(arr))
                return
            
            arr.append(nums[i])
            dfs(i+1,arr)
            arr.pop()
            dfs(i+1,arr)
        
        dfs(0,[])

        return list(res)
            
