'''
104. Maximum Depth of Binary Tree
Given:
Given the root of a binary tree, return its maximum depth.
A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 3
Example 2:
Input: root = [1,null,2]
Output: 2
'''
'''
Solution:
1) if the node is leaf - return 0 for distance addition
2) init max1 and max2 from both child to 1 since the condition to tree to exist is to have at least 1 depth 
3) if the root.right exist , get the max1 from its potomoks and add 1 to it 
4) if the root.left exist, get the max2 from its potomoks and add 1 to it 
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        maxRight = self.maxDepth(root.right) + 1
        maxLeft = self.maxDepth(root.left) + 1

        return max(maxRight, maxLeft)
