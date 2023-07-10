'''
98. Validate Binary Search Tree
Given:
Given the root of a binary tree, determine if it is a valid binary search tree (BST).
A valid BST is defined as follows:
The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 Example 1:
Input: root = [2,1,3]
Output: true
Solution:
The idea is to track the left_limit and right_limit for each node
1) for first node, init them as float('-inf'), float('inf'), to est' pass them as init arugments to inside dfs function when calling from base function 
2) do dfs
3) if not node, return True -> base case
4) if not good with limits, return False
5) if ok, return dfs on left with updated right limit as node.val and dfs on right with updated left limit as node.val
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, left_limit, right_limit):
            if not node:
                return True 

            if not (left_limit < node.val and node.val < right_limit):
                return False 

            return dfs(node.left, left_limit, node.val) and dfs(node.right, node.val, right_limit)

        return dfs(root, float('-inf'),float('inf'))

