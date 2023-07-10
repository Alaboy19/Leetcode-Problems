
'''
Given:
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).
Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
Example 2:
Input: root = [1]
Output: [[1]]
Example 3:
Input: root = []
Output: []
Solution:
1) the idea is to use a deque for node managment 
2) append root to deque initially
3) while deque: 
4) popleft deque from left and append the vals in temp_list and append left and right node to deque
5)append global ans list with each level list 
6) use the number of nodes left in deque as for loop and as start and end of each level 
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = [] 
        q = collections.deque()
        q.append(root)

        while q:
            lenq = len(q)
            level = []
            for i in range(lenq):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                res.append(level)

        return res 
                

