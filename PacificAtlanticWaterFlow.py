'''
417. Pacific Atlantic Water Flow
Given:
There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.
The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).
The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.
Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.
Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
Explanation: The following cells can flow to the Pacific and Atlantic oceans, as shown below:
[0,4]: [0,4] -> Pacific Ocean 
       [0,4] -> Atlantic Ocean
[1,3]: [1,3] -> [0,3] -> Pacific Ocean 
       [1,3] -> [1,4] -> Atlantic Ocean
[1,4]: [1,4] -> [1,3] -> [0,3] -> Pacific Ocean 
       [1,4] -> Atlantic Ocean
[2,2]: [2,2] -> [1,2] -> [0,2] -> Pacific Ocean 
       [2,2] -> [2,3] -> [2,4] -> Atlantic Ocean
[3,0]: [3,0] -> Pacific Ocean 
       [3,0] -> [4,0] -> Atlantic Ocean
[3,1]: [3,1] -> [3,0] -> Pacific Ocean 
       [3,1] -> [4,1] -> Atlantic Ocean
[4,0]: [4,0] -> Pacific Ocean 
       [4,0] -> Atlantic Ocean
Note that there are other possible paths for these cells to flow to the Pacific and Atlantic oceans.
Solution:
0)the idea is to initate dfs from 4 coast lines of oceans 
1) the dfs parameters are dfs(r,c,visitedSet, previousHeight)
2) two sets globally, pacific and atnalitc, intersection is needed for answer
3) base case is when r,c out of bound or when current height is less than prev_height, water can not flow, so -> return
4) recusive case: add cell to visited set and do dfs on four dirs 
5) two for loops and two dfs at each to start dfs from coast lines, according pacific or atlantic set is given as parameter for each dfs in each for loop 
'''
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # dfs(r,c ,visitedSet, prevheight)

        rows, cols = len(heights), len(heights[0])
        pacificSet, atlanticSet = set(), set()

        def dfs(r, c, visitedSet, prevheight):
            #base case 
            if (r,c) in visitedSet or r < 0 or c < 0 or r == rows or c == cols or heights[r][c] < prevheight:
                return 
            visitedSet.add((r,c))

            dfs(r + 1, c, visitedSet, heights[r][c])
            dfs(r - 1, c, visitedSet, heights[r][c])
            dfs(r, c + 1, visitedSet, heights[r][c])
            dfs(r, c - 1, visitedSet, heights[r][c])

        for c in range(cols):
            dfs(0, c, pacificSet, heights[0][c])
            dfs(rows - 1, c, atlanticSet, heights[rows - 1][c])

        for r in range(rows):
            dfs(r, 0, pacificSet, heights[r][0])
            dfs(r, cols - 1, atlanticSet, heights[r][cols - 1])

        final_set = pacificSet.intersection(atlanticSet)

        return [[x,y] for (x, y) in final_set]

