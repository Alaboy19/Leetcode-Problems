'''
78. Subsets
Given:
Given an integer array nums of unique elements, return all possible 
subsets(the power set).The solution set must not contain duplicate subsets. Return the solution in any order.
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Solution:
The idea is to build a decision binary tree whether to include or not include the nums[i] for i from 0 to len(nums) -1
1) so pass to dfs(i), the index of the element
2) if the i > len() append the subset to global ans list
3) if not, append subset by nums[i] and dfs(i+1)
4) when reaches the last, subset pop() and do dfs(i+1) 
dfs(0) and return global_list
'''
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            # decision to include nums[i]
            subset.append(nums[i])
            dfs(i + 1)
            # decision to not include nums[i]
            subset.pop()
            dfs(i + 1)

        dfs(0)
        return res


