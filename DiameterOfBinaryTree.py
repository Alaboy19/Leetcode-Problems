'''
543. Diameter of Binary Tree
Given:
Given the root of a binary tree, return the length of the diameter of the tree.
The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.
The length of a path between two nodes is represented by the number of edges between them.
Example 1:
Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
Example 2:
Input: root = [1,2]
Output: 1
Solution:
The idea is to
1) for each node recursively calculate the max of left or right path and return max of them
2) also update global_max_diam at each node by self.max = max(self.max, maxL + maxR) 
the reason for second point - that maxdiam can be at any level 
3) at head node return the max_diam, at head or not can be tracked with the recur_depth. 
4) if it is not head node, as stated at point 1, return the max of path(left or right) 
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    max_num = 0
    recur_depth = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]):
        self.recur_depth += 1

        if not root:
            return 0

        maxLeft = maxRight = 0     

        if root.left:
            maxLeft = 1 + self.diameterOfBinaryTree(root.left)
        if root.right:
            maxRight = 1 + self.diameterOfBinaryTree(root.right)

        self.max_num = max(self.max_num, maxRight + maxLeft )

        self.recur_depth -= 1

        if self.recur_depth == 0:
            return self.max_num

        return max(maxRight, maxLeft)

