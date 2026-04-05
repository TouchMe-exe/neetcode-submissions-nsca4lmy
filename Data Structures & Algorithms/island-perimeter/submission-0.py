class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        col=len(grid[0])
        row=len(grid)
        count=0
        for i in range (row):
            for j in range (col):
                r,l,u,d=-1,-1,-1,-1

                if j+1<col:
                    r=grid[i][j+1]
                if j-1>-1:
                    l=grid[i][j-1]
                if i+1<row:
                    d=grid[i+1][j]
                    print(d)
                if i-1>-1:
                    u=grid[i-1][j]


                if grid[i][j] == 1:

                    if r==0 or r==-1:
                        count+=1
                        
                    if l==0 or l==-1:
                        count+=1
                        
                    if u==0 or u==-1:
                        count+=1

                    if d==0 or d==-1:
                        count+=1
                     
                
        return count
        