'''
Given:
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.
Each number in candidates may only be used once in the combination.
Note: The solution set must not contain duplicate combinations.
[10,1,2,7,6,1,5], target = 8
Output: 
[[1,1,6],[1,2,5],[1,7],[2,6]]
Solution:
the idea is the same as in subset 2,
0) sorted first
0) decision tree to include nums[i] on left and not include on right
1) the idea is to include the num[i] in sub-tree and not include it to second one, skipping while reaches the different 
num(this is must have since we want to ignore duplicate, since we do not have unique elements given as in combination sum 1)
'''
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = [] 
        subset = [] 
        candidates.sort()

        def dfs(i, total):
            if total == target:
                res.append(subset.copy())
                return
                
            if i >= len(candidates) or total > target:
                return 

            subset.append(candidates[i])
            dfs(i+1, total + candidates[i])
            subset.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i+= 1
            dfs(i+1, total)

        dfs(0, 0)
        return res
