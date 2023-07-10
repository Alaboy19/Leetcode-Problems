'''
90. Subsets II
Given:
Given an integer array nums that may contain duplicates, return all possible 
subsets (the power set)
The solution set must not contain duplicate subsets. Return the solution in any order.
Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
Solution:
This solution has better space-complexity 
1) the idea is the same as in subset 1 problem, except for checking dupilcates before appending 
2) i have used the string of sorted subset to add as a hash to set and check from it 
3) use index and use dfs to include and not include the number in dfs recursion call 
'''
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        str_set = set()

        def dfs(i):
            #base case 
            if i >= len(nums):
                my_subset = sorted(subset)
                string = ''.join(list(map(str, my_subset)))
                if string not in str_set:
                    res.append(subset.copy())
                str_set.add(string)
                return 
            # decision to include
            subset.append(nums[i])
            dfs(i+1)
            # decision to not include
            subset.pop()
            dfs(i+1)

        dfs(0)
        return res

