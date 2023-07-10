

'''
1448. Count Good Nodes in Binary Tree
Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.
Return the number of good nodes in the binary tree.
Example 1:
Input: root = [3,1,4,3,null,1,5]
Output: 4
Explanation: Nodes in blue are good.
Root Node (3) is always a good node.
Node 4 -> (3,4) is the maximum value in the path starting from the root.
Node 5 -> (3,4,5) is the maximum value in the path
Node 3 -> (3,1,3) is the maximum value in the path

Solution:
0) the idea to init res = 1 and dfs left and right passing this res, at each time, new res is 0 or 1 and accumulated
1) inside the func declare dfs that takes node and maxVal that returns accumulation of goods 
2) define base case as return 0 (when hits the none node)
3) res is 1 if node.val >= maxVal and it is incremented recursively on dfs left and dfs right 
4) before passing recursively, update max val and then pass 
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
    
        def dfs(node, maxVal) -> int:
            # base case
            if not node:
                return 0
            # recusive case 
            # res is one and maybe 0, dfs chain of res is like this: 1 + 1 + 0 + 1
            res = 1 if node.val >= maxVal else 0 
            # update maxVal for deeper pass 
            maxVal = max(node.val, maxVal)
            # accumulate the result 
            res += dfs(node.left, maxVal)
            res += dfs(node.right, maxVal)
            return res 

        return dfs(root, root.val)

