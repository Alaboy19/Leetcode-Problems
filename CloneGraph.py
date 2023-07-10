
'''
133. Clone Graph
Given:
Given a reference of a node in a connected undirected graph.
Return a deep copy (clone) of the graph.
Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.
class Node {
    public int val;
    public List<Node> neighbors;
} 
Test case format:
For simplicity, each node's value is the same as the node's index (1-indexed). For example, the first node with val == 1, the second node with val == 2, and so on. The graph is represented in the test case using an adjacency list.
An adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.
The given node will always be the first node with val = 1. You must return the copy of the given node as a reference to the cloned graph
Solution:
0) use nested dfs to copy each node and recursively start copying the neigbors 
1) use hashmap(oldToNew) to track whether node is already copied 
2) dfs has one parameter, node itself
3) base case is if node in hashmap : return new node as oldToNew[node]
4) recursive case: create new node by copy = Node(node.val), then iterate on neighbors and call dfs -> append it to copy.neighbors.append(dfs(each neighbor))
5) return copy node
6) globally call dfs(first_node) and return it, if not node -> return None 
'''
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
import copy
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        oldToNew = {}

        def clone_by_dfs(node):
            # base case 
            if node in oldToNew:
                return oldToNew[node]

            # recusive case 
            copy = Node(node.val)
            oldToNew[node] = copy
            for neig in node.neighbors:
                copy.neighbors.append(clone_by_dfs(neig))
            return copy 
        return clone_by_dfs(node) if node else None  
