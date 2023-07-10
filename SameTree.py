'''
Given:
100. Same Tree
Given the roots of two binary trees p and q, write a function to check if they are the same or not.
Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
Example 1:
Input: p = [1,2,3], q = [1,2,3]
Output: true
Example 2:
Input: p = [1,2], q = [1,null,2]
Output: false
Example 3:
Input: p = [1,2,1], q = [1,1,2]
Output: false

Solution:
the idea is to do a dfs and compare each node to node 
1) as base case, both p and q must not be existed for empty node 
2) if not 1 case, then if one exist and second not return false, also if both exist but values are different -> return false 
3) then if not the 1 case and second case, dig deeper and check 1 and 2 for both (and command) (p.left, q.left) and (p.right, q.right) 
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # recursive call 
        # base case
        if not p and not q:
            return True 

        # recursive case 1 
        if (not p and q) or (not q and p) or p.val != q.val:
            return False 


        # return statement
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
