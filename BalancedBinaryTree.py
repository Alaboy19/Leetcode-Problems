'''
110. Balanced Binary Tree
Given:
Given a binary tree, determine if it is 
height-balanced
.Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: true
Example 2:
Input: root = [1,2,2,3,3,null,null,4,4]
Output: false

Solution:
the idea is as in the maximum depth problem
1) at each node calculate the max path of childs 
2) at each node update the global self.max_diff variable 
3) dfs returns the max of the childs and whether the current self.max_diff is less or qual to 1 
4) run the 3) at head node 
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    maxDiff = 0 
    def isBalanced(self, root: Optional[TreeNode])-> bool:
        return self.recur_path_diff(root)[1]

    def recur_path_diff(self, root: Optional[TreeNode]):
        # base case when poped at None after leaf
        if not root:
            return 0, self.maxDiff <= 1
        # recursive case right 
        maxRight = 1 + self.recur_path_diff(root.right)[0]
        # recursive case left 
        maxLeft = 1 + self.recur_path_diff(root.left)[0]
        # update global maxDiff variable 
        self.maxDiff = max(self.maxDiff, abs(maxLeft - maxRight))
        
        
        return max(maxLeft, maxRight), self.maxDiff <= 1

