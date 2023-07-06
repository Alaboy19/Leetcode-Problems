'''
189. Rotate Array - Medium
Given:
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
'''
'''
Solution:
The overall idea is to perform reversals with two pointer
0) reverse the entire list
1) reverse from 0 to k - 1
2) reverse from the k to len(nums) - 1
'''
def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.

        """
        # res = [0] * len(nums)

        # for i in range(len(nums)):
        #     res[(i + k) % len(nums)] = nums[i]
        # print(res)
        
        # for i in range(len(res)):
        #     nums[i] = res[i]
        k = k % len(nums)
        self.reverse(nums, 0, len(nums) - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, len(nums) -1) 


    def reverse(self, nums, l, r):
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l + 1, r - 1
