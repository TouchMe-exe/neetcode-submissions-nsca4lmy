class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        rows=len(heights)
        cols=len(heights[0])
        trigger=[0,0]
        pac,alt=set(),set()
        res=[]

        def dfs(i,j,prev_val,visited):

            if i<0 or j<0 or i>=rows or j>=cols:
                return
            if (i,j) in visited:
                return
            if heights[i][j]<prev_val:
                return

            visited.add((i,j))
            val=heights[i][j]
            dfs(i+1,j,val,visited)
            dfs(i-1,j,val,visited)
            dfs(i,j+1,val,visited)
            dfs(i,j-1,val,visited)

        
        for c in range(cols):
            dfs(0,c,heights[0][c],pac)
            dfs(rows-1,c,heights[rows-1][c],alt)
            
        for r in range(rows):
            dfs(r,0,heights[r][0],pac)
            dfs(r,cols-1,heights[r][cols-1],alt)

        for i in range(rows):
            for j in range(cols):
                if (i,j) in pac and (i,j) in alt:
                    res.append([i,j])
        
        return res
        



