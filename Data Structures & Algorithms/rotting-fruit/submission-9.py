class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])
        fresh = 0
        rotten = 0
        q = deque()
        visited = set()
        time = -1
        directions = [[1,0], [-1,0], [0,-1], [0,1]]

        def bfs_helper(node):
            nonlocal fresh
            r, c = node
            for u, v in directions:
                if r + u < 0 or r + u > rows - 1 or c + v < 0 or c + v > cols - 1:
                    continue

                if grid[r + u][c + v] == 1:
                    grid[r + u][c + v] = 2
                    q.append((r + u, c + v))
                    fresh -= 1

        

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    q.append((i,j))
                    rotten += 1
        
        while q:
            layer = len(q)
            for i in range(layer):
                node = q.popleft()
                bfs_helper(node)

            time += 1
            

        if fresh == 0:
            return max(time, 0)

        return -1



