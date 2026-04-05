class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        rows=len(heights)
        cols=len(heights[0])
        trigger=[0,0]
        res=[]

        def dfs(i,j,val,visited):

            if i<0 or j<0:
                trigger[0]=1
                return
            if i>=rows or j>=cols:
                trigger[1]=1
                return

            if heights[i][j]>val or (i,j) in visited :
                return
            if trigger[0]==1 and trigger[1]==1:
                return
            

            visited.add((i,j))
            val=heights[i][j]
            dfs(i+1,j,val,visited)
            dfs(i-1,j,val,visited)
            dfs(i,j+1,val,visited)
            dfs(i,j-1,val,visited)
            #visited.remove((i,j))

        
        for i in range(rows):
            for j in range(cols):
                trigger=[0,0]
                dfs(i,j,1001,set())
                if trigger[0]==1 and trigger[1]==1:
                    res.append([i,j])
        
        return res
        



