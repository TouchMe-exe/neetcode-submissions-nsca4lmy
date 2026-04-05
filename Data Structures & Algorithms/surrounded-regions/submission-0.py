class Solution:
    def solve(self, board: List[List[str]]) -> None:
        row=len(board)
        col=len(board[0])
        visited=set()
        temp=[]
        
        def dfs(i,j):

            if (i,j) in visited:
                return
            if i==row or j==col or i<0 or j<0:
                return
            if board[i][j]=='X':
                return
            
            visited.add((i,j))
            board[i][j]='T'
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)


        for i in range(col):
            dfs(0,i)
            dfs(row-1,i)
        for i in range(row):
            dfs(i,0)
            dfs(i,col-1)
        
        for i in range (row):
            for j in range(col):
                if board[i][j]=='O':
                    board[i][j]='X'
                if board[i][j]=='T':
                    board[i][j]='O'
        
        

