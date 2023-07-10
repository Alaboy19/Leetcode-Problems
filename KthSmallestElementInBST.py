'''
230. Kth Smallest Element in a BST
Given:
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.
Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3
Solution:
The idea is to do dfs, but remember the stack call on stack iteratevly, this is needed to pop from stack when there is no left node and only right node or no both nodes, using the structure of binary tree and pop when no left node, we can construct(when poped from list) the sorted list from less to greater 
1) Try to go left and append to stack when root is not none 
2) if root is none, pop the last on stack (append to list the val) and iterate to his right 
3) do the 1 again, when we try to pop from the emplty stack, it means that we reached the end of the bst -> throw a break 
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        my_list = []
        while True:
            if root:
                stack.append(root)
                root = root.left
            else:
                if not stack:
                    break
                last_node = stack.pop()
                my_list.append(last_node.val)
                root = last_node.right
        return my_list[k-1]

