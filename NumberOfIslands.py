'''
200. Number of Islands
Given:
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
You may assume all four edges of the grid are all surrounded by water.
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
Solution:
BFS solution
0) idea is to have a deque and append parent nodes and extract leftmost parent and process its child and add them to queue and do all this thing while there is a deque
1) the solving idea is the same as in dfs, we iterate through the matrix and mark visited nodes, when whenever we start bfs or dfs on some "1" node, we iterate islands+= 1
2) when we popleft from q, we go four direction if it is possible, up, down, left, right by incrementing r, c for [[1,0][0,1][-1,0][0,-1]] and add to visited
3) it is not a recursive algorithm, so no base case and recursive case 
4) the condition for adding to queue and adding to visited is 
 if (r in range(rows) and c in range(cols)
    and (r,c) not in visited and grid[r][c] == "1"): 
'''
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        visited = set()

        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])

        def bfs(r, c):
            q = deque()
            visited.add((r, c))
            q.append((r, c))
            

            while q:
                row, col = q.popleft()
                dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in dirs:
                    r, c = row + dr, col + dc
                    if (r in range(rows) and c in range(cols)
                     and (r,c) not in visited and grid[r][c] == "1"): 
                
                        q.append((r, c))
                        visited.add((r, c))


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    bfs(r,c)
                    islands += 1

        return islands

