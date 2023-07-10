'''
994. Rotting Oranges
Given:
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.
Example 1:
Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4

Solution:
the same problem as walls and gates 
0) the general idea is to get start from rotten and assagin value(init=3) and go four direction with incremented value and assign and keep doing it recursively
1) the base case is when in bound of rows, cols or 0(empty) or (2 and nums!=3) or (r,c in visited and [r][c] <= num) -> return (the last check is to update from antoher rotten if less distance found), (2 and nums!=3) is to check whether from one rotten to antoher rotten came -> need to pop back
2) in order to mark visited cells, just use dfs 
3) recursive case: add to visited, mark [r][c] with val and go dfs four dirs
4) in global function, iterate nested for loop and if [r][c] == 2 and not in visited -> call dfs()
5) if one fresh found - > return -1
6) get the max_num of cells and substract 3 and return it 
'''
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ans = 0 
        visited = set()
        rows, cols = len(grid), len(grid[0])

        def dfs(r,c, num):
            # base case 
            if (r not in range(rows) 
            or c not in range(cols) 
            or grid[r][c] == 0 
            or (grid[r][c] == 2 and num != 3) 
            or ((r,c) in visited and grid[r][c] <= num)
            ):
                return 
            # recursive case 
            visited.add((r,c))
            grid[r][c] = num
           
            dfs(r, c + 1, num + 1)
            dfs(r, c - 1, num + 1)
            dfs(r + 1, c, num + 1)
            dfs(r - 1, c, num + 1)
           

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2 and (r,c) not in visited:
                    dfs(r,c, 3)
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return -1

        max_num = 3

        for r in range(rows):
            for c in range(cols):
                max_num = max(max_num, grid[r][c])

        

        return max_num - 3

