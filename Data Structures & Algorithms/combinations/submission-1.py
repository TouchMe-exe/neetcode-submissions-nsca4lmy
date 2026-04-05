class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        arr=[i for i in range(1,n+1)]
        res=[]

        def dfs(i,cur_arr):

            if len(cur_arr) == k:
                res.append(cur_arr[:])
                return

            if i==len(arr):
                return
            
            cur_arr.append(arr[i])
            dfs(i+1,cur_arr)
            cur_arr.pop()
            dfs(i+1,cur_arr)

        dfs(0,[])

        return res

            
