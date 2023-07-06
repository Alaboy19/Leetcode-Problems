'''
287. Find the Duplicate Number - Medium
Given:
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
There is only one repeated number in nums, return this repeated number.
You must solve the problem without modifying the array nums and uses only constant extra space.

Example 1:
Input: nums = [1,3,4,2,2]
Output: 2
Example 2:

Input: nums = [3,1,3,4,2]
Output: 3
'''
'''
Solution:
0) The linear time solution is to use counting sort
1) create a O(n) space - list with idx for num in nums
2) iterate through the nums and fill countsort by idx-num and value as occurrence
3) then iterate through counting sort and return when it is more than 1 
4) return None as default case just to be safe  
'''

def findDuplicate(self, nums: List[int]) -> int:
        countsort = [0] * (len(nums))

        for num in nums:
            countsort[num] += 1

        for i in range(len(countsort)):
            if countsort[i] > 1:
                return i 
        return None 
