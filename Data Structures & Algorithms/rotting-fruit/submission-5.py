class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        rows=len(grid)
        cols=len(grid[0])
        time=0
        fresh=0
        q=deque()
        visited=set()

        def bfs(i,j):

            if i<0 or j<0 or i>=rows or j>=cols or grid[i][j]==0:
                return 
            if (i,j) in visited:
                return 
                
            q.append([i,j])
            visited.add((i,j))
            

        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1:
                    fresh+=1
                if grid[i][j]==2:
                    q.append([i,j])
                    visited.add((i,j))


        while q and fresh>0:
            
            for index in range(len(q)):
                i,j=q.popleft()
                if grid[i][j]==1:
                    fresh-=1
                bfs(i+1,j)
                bfs(i-1,j) 
                bfs(i,j+1) 
                bfs(i,j-1)
            if q:
                time+=1

        
        return time if fresh==0 else -1
