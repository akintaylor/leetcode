def dfs(board, i , j):
    row = len(board)
    col = len(board[0])
    
    if i == row or j == col or i < 0 or j < 0 or board[i][j] != 'O':
        return
    
    board[i][j] = '#'
    
    dfs(board, i, j - 1)
    dfs(board, i, j + 1)
    dfs(board, i - 1, j)
    dfs(board, i + 1, j)
        
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row = len(board)
        col = len(board[0])
        
        # rows
        for i in range(col):
            if board[0][i] == 'O':
                dfs(board, 0, i)
            if board[-1][i] == 'O':
                dfs(board, row - 1, i)
        
        # col
        for i in range(row):
            if board[i][0] == 'O':
                dfs(board, i, 0)
            if board[i][-1] == 'O':
                dfs(board, i, col - 1)
                
        for i in range(row):
            for j in range(col):
                if board[i][j] == '#':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'
                    
        
        
                

            
