'''
130. Surrounded Regions
Given:
Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.
A region is captured by flipping all 'O's into 'X's in that surrounded region.
Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
Explanation: Notice that an 'O' should not be flipped if:
- It is on the border, or
- It is adjacent to an 'O' that should not be flipped.
The bottom 'O' is on the border, so it is not flipped.
The other three 'O' form a surrounded region, so they are flipped.

Solution:
0) the clever idea is to mark unsurrounded regions of "0" and then iteratively just flip others that are not marked
1) the idea is to start dfs from four borders and add to visited the unsorrounded "0" regions 
2) the dfs(r,c) and base case is when r and c out of bound, r,c in visited and board[r][c] == "X" -> return 
3) recusive case is to add to visited (r,c) and go dfs four four dirs 
4) for c in range(COLS) ->  dfs(0, c); dfs(ROWS - 1, c)
5) for r in range(ROWS) ->  dfs(r,0) ; dfs(r, COLS - 1)
6) just flip all other "0" that are not in visited
'''
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS, COLS = len(board), len(board[0])
        visited = set()

        def dfs(r,c):
            #base case:
            if r not in range(ROWS) or c not in range(COLS) or (r,c) in visited  or board[r][c] == "X":
                return

            visited.add((r,c))
            dfs(r, c + 1)
            dfs(r, c - 1)
            dfs(r + 1, c)
            dfs(r - 1, c) 

        for c in range(COLS):
           dfs(0, c)
           dfs(ROWS - 1, c)

        for r in range(ROWS):
            dfs(r,0)
            dfs(r, COLS - 1)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O" and (r,c) not in visited:
                    board[r][c] = "X"

    


