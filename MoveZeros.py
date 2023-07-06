'''
283. Move Zeroes
Given:
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.
Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
'''
'''
Solution:
1) count the occurence of the zeros
2) just iterate through array and modify it in place, by placing non-zero elements from idx 0
3) second point is OK since at worst scenarios, with no zeros, each value will be assigned to his own idx
4) then pop everything at the back since it is garbage 
5) append zeros for that amount that we know from zero_count from 1 point 
'''

def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count_zeros = 0 
        for num in nums:
            if num == 0:
                count_zeros += 1

        idx_to_place = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[idx_to_place] = nums[i]
                idx_to_place += 1
        
        for i in range(count_zeros):
            nums.pop()

        for i in range(count_zeros):
            nums.append(0)
