'''
39. Combination Sum
Given:
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.
The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.
The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.
Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.
Solution:
The idea is to do the dfs while it reaches the target sum 
1) firstly, we do dfs on left by dfs(i), itself
2) secondly, we do dfs on right by dfs(i+1), adding the next num 
3) we pop after 1 and before 2, 
4) also we will count sum
5) two base case, when out of limit and when total reaches the sum 
'''
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def dfs(i, cur, total):
            # first base case when passed total is equal to target 
            # in this case we need to append and return 
            if total == target:
                result.append(cur.copy())
                return
            # second base case is when index is more than lenth of candidate or when 
            # total is more than target - > this way is nowhere
            if i >= len(candidates) or total > target:
                return

            # if base case is not meet, we append cur list with candidates[i]

            cur.append(candidates[i])
            
            # then dfs on i and pass current list and total sum 
            dfs(i, cur, total + candidates[i])
            # this path leads to the number addition itself, so in order to have another option with
            # next value pop it 
            cur.pop()
            # call on i+1
            dfs(i + 1, cur, total)

        # pass as init value: i = 0, curr_list = [], total = 0 
        dfs(0, [], 0)
        # return global result 
        return result

