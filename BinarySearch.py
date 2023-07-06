'''
704. Binary Search - Easy
Given:
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.
You must write an algorithm with O(log n) runtime complexity.
Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
'''

'''
Solution:
use lbinsearch with condition of >= to find the first condition mathcing the condition 
'''

def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        idx = self.leftbinSearch(l, r, nums, target)
        if nums[idx] != target:
            return -1
        return idx
    
    def leftbinSearch(self, l, r, nums, target):
        while l < r:
            mid = (l + r) // 2
            if nums[mid] >= target:
                r = mid
            else:
                l = mid + 1
        return l
