'''
286. Walls and Gates
Given:
You are given an m x n grid rooms initialized with these three possible values.
-1 A wall or an obstacle.
0 A gate.
INF Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.
Input: rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
Output: [[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]
Solution:
0) the general idea is to get start from gate and assagin value(init=0) and go four direction with incremented value and assign and keep doing it recursively
1) the base case is when in bound of rows, cols or -1 or (0 and val!=0) or (r,c in visited and [r][c] <= num) -> return (the last check is to update from antoher gat if less distance found), (0 and val!=0) is to check whether from one gate to antoher gate came -> need to pop back
2) in order to mark visited cells, just use dfs 
3) recursive case: add to visited, mark [r][c] with val and go dfs four dirs
4) in global function, iterate nested for loop and if [r][c] == 0 and not in visited -> call dfs()
'''
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        visited = set()
        rows, cols = len(rooms), len(rooms[0])

        def dfs(r,c, num):
            # base case 
            if (r not in range(rows) 
            or c not in range(cols) 
            or rooms[r][c] == -1 
            or (rooms[r][c] == 0 and num != 0) 
            or ((r,c) in visited and rooms[r][c] <= num)
            ):
                return 
            # recursive case 
            visited.add((r,c))
            rooms[r][c] = num
           
            dfs(r, c + 1, num + 1)
            dfs(r, c - 1, num + 1)
            dfs(r + 1, c, num + 1)
            dfs(r - 1, c, num + 1)
           

        for r in range(rows):
            for c in range(cols):
                if rooms[r][c] == 0 and (r,c) not in visited:
                    dfs(r,c, 0)

