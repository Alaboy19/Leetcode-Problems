'''
572. Subtree of Another Tree
Given:
Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.
A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.
Example 1:
Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true
Example 2:
Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
Output: false

Solution:
the idea is to iterate dfs-ly and if the value are equal to subroot value -> 
1) run the function from the prev question with same tree function 
2) if same tree -> stop and return the glob variable 
3) default return is false 
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    return_val = False
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        self.dfs(root, subRoot)
        return self.return_val 
    
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True

        elif (not p and q) or (not q and p) or (p.val != q.val):
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

    def dfs(self, root: Optional[TreeNode], subRoot: Optional[TreeNode])-> None:
        if not root:
            return 

        if root.val == subRoot.val and self.isSameTree(root, subRoot):
            self.return_val = True
            return 

        self.dfs(root.left, subRoot)
        self.dfs(root.right, subRoot)
