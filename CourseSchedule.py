'''
207. Course Schedule
Given:
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. 
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.
For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.
Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.
Solution:
0)  the idea is to find the loop by having a visitingset, when pop back - exclude from set, so if new path to the point - > loop
1) firstly, convert info to adjacent list with vertex and neighbors as v : [neighbor1, beighbor2]
2) dfs(vertex) -> base case: if vertex in still visiting set  - > return false
3) second base case: if [vertex] is empty -> return True 
4) recusive case: add this to still visiting set and run dfs by for loop on neighbors: if not (dfs): return False
5) if everythin is ok with neighbors, if returned true , then remove it from the still visiting and mark this line as ok by making preReq[vertex] = [], then return True(pop back) 
6) call dfs on each vertex of the graph in case there is an undirected graph 
7) call by for loop and if not dfs: return False, default - > return True 
'''
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preReq = {i: [] for i in range(numCourses)}

        for vertex, toVertex in prerequisites:
            preReq[vertex].append(toVertex)

        stillVisiting = set()

        def dfs(vertex):
            # base case when found loop
            if vertex in stillVisiting:
                return False
            # base case when have reached a dead-end
            if preReq[vertex] == []:
                return True 

            stillVisiting.add(vertex)

            for neighbors in preReq[vertex]:
                if not dfs(neighbors): 
                    return False 
            
            stillVisiting.remove(vertex)

            preReq[vertex] = []

            return True 

        for vertex in range(numCourses):
            if not dfs(vertex): 
                return False 

        return True 
        



