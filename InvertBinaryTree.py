'''
226. Invert Binary Tree
Given:
Given the root of a binary tree, invert the tree, and return its root.
Example 1:
Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]
Example 2:
Input: root = [2,1,3]
Output: [2,3,1]
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        '''the key thing here is to define a base case by if root exist, if not     return None
                else:
                1) we swap left to right
                2) call this recursively on left 
                3) call this recursivly on right '''

        # base case 

        # recursive case 1 
        # recursive case 2 

        if not root:
            return None 

        tempNode = root.left
        root.left = root.right
        root.right = tempNode

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
'''
Solution:
the key thing here is to define a base case by if root exist, if not return None
else:
1) we swap left to right
2) call this recursively on left 
3) call this recursivly on right 
4) return root 
'''

