'''
Given:
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Solution:
0) my solution - it is a bruteforce 
1) the idea is to include each number and next level exclude this number from candidates 
2) base case is when len(curr) == len(nums) -> append global result by copy of curr list
3) recursive case: for num in nums: if num in curr: continue else cur.append(num), dfs(curr), curr.pop()
4) cal dfs on [], return res 
'''
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        # base case 
        def dfs(curr):
            if len(curr) == len(nums):
                result.append(curr.copy())
                return 
            
            for num in nums:
                if num in curr:
                    continue 
                curr.append(num)
                dfs(curr)
                curr.pop()

        dfs([])
        return result

        #base case
        # if len(nums) == 1:
        #     return [nums.copy()]
        
        # for i in range(len(nums)):
        #     n = nums.pop(0)
        #     perms = self.permute(nums)
            
        #     for perm in perms:
        #         perm.append(n)
        #     result.extend(perms)
        #     nums.append(n)
            
        # return result
