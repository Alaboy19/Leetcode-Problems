'''
35. Search Insert Position
Given:
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
You must write an algorithm with O(log n) runtime complexity.
Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
'''

'''
Solution:
we find leftbinsearch on first occurrence of >= target,
and then check whether it is it or the first  one that greater than target (this case also covers when target is not present at all)
'''

def searchInsert(self, nums: List[int], target: int) -> int:
        l = self.lbinsearch(nums, target)
        if nums[l] < target:
            return l + 1
        return l 

    def lbinsearch(self, nums, target):
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] >= target:
                r = mid
            else:
                l = mid + 1
        return l
