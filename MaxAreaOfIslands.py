'''
695. Max Area of Island
Given:
0) the general idea is to get one islands and enter it and mark every cell to visited and keep iteratating thorugh
matrix until stuck to new, non visited 1 cell
1) before entering the cell, remember the value of max_area_island, then after leaving, compare with difference and assign new max_area_island
2) in order to mark visited cells, just use dfs 
3) the logic of dfs(r,c) -> base case-> if r,c out of bound and is 0 and in visited -> return
recursive cae -> visited.add(),  dfs(up), dfs(down), dfs(left), dfs(right)
Solution:

'''

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans = 0
        visited = set()

        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])

        def dfs(r,c):
            # base case 
            if (r not in range(rows) 
            or c not in range(cols) 
            or grid[r][c] == 0 
            or (r,c) in visited
            ):
                return 
            # recursive case 
            visited.add((r,c))
           
            dfs(r, c + 1)
            dfs(r, c - 1)
            dfs(r + 1, c)
            dfs(r - 1, c)
           

        for r in range(rows):
            for c in range(cols):
                length_before = len(visited)
                if grid[r][c] == 1 and (r,c) not in visited:
                    dfs(r,c)
                    ans = max(len(visited) - length_before, ans)

        return ans
