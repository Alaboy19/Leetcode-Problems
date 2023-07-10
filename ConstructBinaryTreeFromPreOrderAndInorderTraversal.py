'''
105. Construct Binary Tree from Preorder and Inorder Traversal
Given:
Given two integer arrays preorder and inorder where preorder 
is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.
Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]
Solution:
The idea is to use the feature of the preorder that its first value is the start node
1) then find this start node in inorder, where it is divides the left subtree and rightsubtree
2) use this info and recursively build left and right surbtrees passing the left subtree and right subtree preorder and inorder lists by list partitioning 
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return
        root_val = preorder[0]
        root = TreeNode(root_val)
        mid = inorder.index(root_val)
        root.left = self.buildTree(preorder[1: mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])
        return root
