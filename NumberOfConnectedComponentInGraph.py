'''
Number of Connected Components in an Undirected Graph
Given:
You have a graph of n nodes. You are given an integer n and an array edges where edges[i] = [ai, bi] indicates 
that there is an edge between ai and bi in the graph.
Return the number of connected components in the graph.

Input: n = 5, edges = [[0,1],[1,2],[3,4]]
Output: 2
Solution:
0) firslty convert the given info to graph hashmap with vertex and list of edges 
1) delcare visited set globally
2) idea is to dfs and count globally how many times we exected dfs on vertices 
3) the number of dfs executed is the number of connected components since dfs reach until connected components
4) in order to mark all the vertex traversed, we use visited set
5) base case for dfs is if vertex in visited -> return 
6) recusive case -> add to visited and call dfs on each neighobors if their are not in visited already
7) globally iterate On vertices and call dfs if not in visited, and count this line execution
8) return count  
'''
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        count = 0
        visited = set()

        graph = {i : [] for i in range(n)}

        for vertex1, vertex2 in edges:
            graph[vertex1].append(vertex2)
            graph[vertex2].append(vertex1)    

        def dfs(vertex):
            # base case 
            if vertex in visited:
                return 
            
            visited.add(vertex)
            
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    dfs(neighbor)

        for vertex in graph: 
            if vertex not in visited:
                count += 1 
                dfs(vertex)

        return count 

