'''
36. Valid Sudoku - Medium
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
'''


'''
Solution:
1) iterate colonwise check for repetition by set space 
2) iterate rowwise and check for repetition by set space 
3) do the same for each 9 block iterating I from 0,3,6 
'''
def isValidSudoku(self, board: List[List[str]]) -> bool:
        ans = True
        for i in range(9):
            myset = set()
            for j in range(9):
                if board[i][j] != '.':
                    if board[i][j] not in myset:
                        myset.add(board[i][j])
                    else:
                        ans = False

        for j in range(9):
            myset = set()
            for i in range(9):
                if board[i][j] != '.':
                    if board[i][j] not in myset:
                        myset.add(board[i][j])
                    else:
                        ans = False

        for x in range(0,9,3):
            for y in range(0,9,3):
                myset = set()
                for i in range(x, x + 3):
                    for j in range(y, y + 3):
                        if board[i][j] != '.':
                            if board[i][j] not in myset:
                                myset.add(board[i][j])
                            else:
                                ans = False

        return ans
