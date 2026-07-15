class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [[] for _ in range(9)]
        columns = [[] for _ in range(9)]
        grids = [[] for _ in range(9)]

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] != ".":
                    rows[i].append(board[i][j])
                    columns[j].append(board[i][j])
                    
                    if j < 3:
                        if i < 3:
                            grids[0].append(board[i][j])
                        elif i < 6:
                            grids[1].append(board[i][j])
                        else:
                            grids[2].append(board[i][j])
                    elif j < 6:
                        if i < 3:
                            grids[3].append(board[i][j])
                        elif i < 6:
                            grids[4].append(board[i][j])
                        else:
                            grids[5].append(board[i][j])
                    else:
                        if i < 3:
                            grids[6].append(board[i][j])
                        elif i < 6:
                            grids[7].append(board[i][j])
                        else:
                            grids[8].append(board[i][j])
        
        for i in range(9):
            if len(set(rows[i])) != len(rows[i]):
                return False
            if len(set(columns[i])) != len(columns[i]):
                return False
            if len(set(grids[i])) != len(grids[i]):
                return False
        return True