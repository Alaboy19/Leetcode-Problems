'''
199. Binary Tree Right Side View
Given:
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.
Example 1:
Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]
Example 2:
Input: root = [1,null,3]
Output: [1,3]

Solution:
the idea is to just get the bfs from binary tree level order traversal quesiton 
0) use global res list and deq to track and manage the proceses with nodes
0.1) init the deq with the root -> only one node
0.2) iterate through deq with while deq and for loop till len(deq):
0.3) at each level deq will pop the level upper and fill it with level down
4) then just use the last unit of the level if level exists and append to res at each level
5) return the rest list 
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        deque = collections.deque()
        deque.append(root)
        

        while deque:
            lendeq = len(deque)
            #level = []

            for i in range(lendeq):
                node = deque.popleft()
                if node and (i == lendeq - 1):
                    deque.append(node.left)
                    deque.append(node.right)
                    res.append(node.val)
                    

            # if level:
            #     res.append(level.pop())

        return res 
