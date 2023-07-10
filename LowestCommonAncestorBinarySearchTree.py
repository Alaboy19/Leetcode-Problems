'''
235. Lowest Common Ancestor of a Binary Search Tree - Medium
Given:
Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.
According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”
Example 1:
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.

Solution:
the idea is to 
1) make LCA equal to root for init
1.1) and two compare with values of p.val and q.val and LCA.val to know whether less LCA lays 
in left direction or right direction  
2) if both value to left, lca.left
3) if both value to right, lca.right
4) iterate while holds 2, 3, if not, return lca straiht away 
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ''''''
        lca = root
        while lca:
            if p.val < lca.val and q.val < lca.val:
                lca = lca.left
            elif p.val > lca.val and q.val > lca.val:
                lca = lca.right
            else:
                return lca 
