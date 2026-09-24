class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for  i in range(len(board)):
            num=set()
            for j in range(len(board[0])):
                if(board[i][j]!="."):
                    if(int(board[i][j])>9):
                        return False
                    if board[i][j]  in num:
                        return False
                    num.add(board[i][j])
        for i in range(len(board[0])):
            num1=set()
            for j in range(len(board)):
                if(board[j][i]!="."):
                    if(int(board[j][i])>9):
                        return False
                    if board[j][i] in num1:
                       return False
                    num1.add(board[j][i])
        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                num = set()
                for i in range(row, row + 3):
                    for j in range(col, col + 3):
                        if board[i][j] != ".":
                            if board[i][j] in num:
                                return False
                            num.add(board[i][j])
        return True
