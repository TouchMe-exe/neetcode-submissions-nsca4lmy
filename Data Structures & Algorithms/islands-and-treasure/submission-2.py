class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        rows=len(grid)
        cols=len(grid[0])
        visited=set()
        q=deque()
        


        def bfs(i,j):
            if i<0 or j<0 or i>=rows or j>=cols or grid[i][j]==-1:
                return  
            if (i,j) in visited:
                return 
            q.append([i,j])
            visited.add((i,j))

            
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==0:
                    q.append([i,j])
                    visited.add((i,j))
        

        dist=0
        while q:
            for index in range(len(q)):
                i,j=q.popleft()
                grid[i][j]=dist
                bfs(i+1,j)
                bfs(i-1,j)
                bfs(i,j+1)
                bfs(i,j-1)
            dist+=1


        