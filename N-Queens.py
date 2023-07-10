'''
N-Queens - Hard
Given:
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.
Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.
Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.
Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above
Solution:
The idea is to dfs on row wise 
1) base case when we reach the fourth row it means when over board -> return 
2) at each dfs recursive call -> we iterate by column and call dfs at each col, also
3) at each col, we check conditions whether this column is ok or not, by comparing col_set, posDiag, negDiag
3) if good, we add info to col_set, posDiagm negDiag and place the queen and dfs on next row, if not ok,  continue on the next column 
'''
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = [] 
        col = set()
        posDiag = set()
        negDiag = set()
        board = [["."] * n for i in range(n)]
        
        def dfs(i):
            # base case 1
            if i == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return

            for j in range(n):
                if j in col or i-j in negDiag or i+j in posDiag:
                    continue 

                col.add(j)
                negDiag.add(i-j)
                posDiag.add(i+j)
                board[i][j] = "Q"

                # dfs call 
                dfs(i+1)

                col.remove(j)
                negDiag.remove(i-j)
                posDiag.remove(i+j)
                board[i][j] = "."

        dfs(0)
        return res 

