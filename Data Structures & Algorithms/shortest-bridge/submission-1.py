class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        direction = [[1,0],[0,1],[-1,0],[0,-1]]
        q = deque()
        found = False

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    start = [i,j]
                    found = True
                    break
            if found == True:
                break
    

        def dfs(i, j):
            if i < 0 or j < 0 or i >= n or j >= m or grid[i][j] != 1:
                return

            grid[i][j] = 2
            q.append((i,j))

            for u,v in direction:
                dfs(i+u, j+v)
        

        def bfs(node):
            i,j = node
            for u, v in direction:
                if i+u < 0 or j+v < 0 or i+u >= n or j+v >= m:
                    continue
                if grid[i+u][j+v] == 2:
                    continue
                if grid[i+u][j+v] == 1:
                    return False
                grid[i+u][j+v] = 2
                q.append((i+u,j+v))

            return True

        dfs(start[0], start[1])
        res = 0
        
        while q:
            len_q = len(q)
            for i in range(len_q):
                node = q.popleft()
                if not bfs(node):
                    return res
            res += 1



                


        




            
            
            