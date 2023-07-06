'''
33. Search in Rotated Sorted Array - Medium
Given:
There is an integer array nums sorted in ascending order (with distinct values).
Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].
Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.
You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
'''
'''
Solution:
firstly, I find the pivot idx and then execute two left bin search 
'''
def search(self, nums: List[int], target: int) -> int:
        pivot_idx = self.binsearch_broken_array(0, len(nums) - 1, nums)
        tgt_idx_1 = self.leftbinSearch(0, pivot_idx - 1, nums, target)
        if nums[tgt_idx_1] != target:
            tgt_idx2 = self.leftbinSearch(pivot_idx, len(nums) - 1, nums, target)
            if nums[tgt_idx2] != target:
                return -1
            return tgt_idx2
        return tgt_idx_1


    def leftbinSearch(self, l, r, nums, target):
        while l < r:
            mid = (l + r) // 2
            if nums[mid] >= target:
                r = mid
            else:
                l = mid + 1
        return l

    def check(self, m, checkparams):
        nums, r = checkparams
        return nums[m] > nums[r]


    def binsearch_broken_array(self, l, r, nums):
        while l < r:
            m = (l + r) // 2
            if self.check(m, (nums, r)):
                l = m + 1
            else:
                r = m
        return l
