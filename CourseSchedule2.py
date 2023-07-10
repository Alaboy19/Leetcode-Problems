'''
210. Course Schedule II
Given:
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. 
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.
For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. 
If it is impossible to finish all courses, return an empty array.
Solution:
0) use dfs to recursively traverse the graph and take into account the cycle
1) declare visited and still visiting set 
2) get adjacent list from input
3) dfs(vertex), base case: if in stillvisiting -> False, if in visited return True 
4) recursive case: add to stillvisiting, call on neighbors 
5) or neig in preReq[vertex]:
          if dfs(neig) == False:
                    return False
            stillVisiting.remove(vertex)
            visited.add(vertex)
            output.append(vertex)
6) return True 
'''
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preReq = {i: [] for i in range(numCourses)}

        visited, stillVisiting = set(), set()
        output = []

        for course, preCourse in prerequisites:
            preReq[course].append(preCourse)

        def dfs(vertex):
            # base case one when detected cycle
            if vertex in stillVisiting:
                return False
            # base case two when just already visited
            if vertex in visited:
                return True 

            # recursive case -> add to current path 
            stillVisiting.add(vertex)
            # recussively call for each neigh -> if cycle detected in subpath -> return False
            for neig in preReq[vertex]:
                if dfs(neig) == False:
                    return False
            # when getting out of the path, remove from stillvisiting and add to visited and 
            # output answer 
            stillVisiting.remove(vertex)
            visited.add(vertex)
            output.append(vertex)

            return True 

        for vertex in range(numCourses):
            if not dfs(vertex):
                return []

        return output
