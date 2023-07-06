'''
15. 3Sum - Medium
Given:
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.
Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

'''
'''
Solution:
1) the overall logic is to sort first and use the idea from two sum II problem with two pointer
2) we escape duplicate by if nums [i] == nums [i-1] : continue
3) for each i, we will assign l,r as i+1, len(nums) -1
4) then , will check for sum, if sum is more, r-=1, if less, l+=1
5) if summ is target, append ans and l+=1, r-=1, then while l at duplicate, l+=1 again

'''

def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []

        for i in range(len(nums) - 2):
            if nums[i] > 0:
                break
            if i >= 1 and nums[i] == nums[i - 1]:
                continue
            
            l, r = i + 1, len(nums) - 1
            while l < r:
                if nums[i] + nums[l] + nums[r] == 0:
                    ans.append([nums[i], nums[l], nums[r]])
                    l, r = l + 1, r - 1
                    while nums[r] == nums[r + 1] and l < r:
                        r -= 1
                elif nums[i] + nums[l] + nums[r] < 0:
                    l += 1 
                else:
                    r -= 1

        return ans
