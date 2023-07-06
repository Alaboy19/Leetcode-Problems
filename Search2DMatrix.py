'''
74. Search a 2D Matrix
Given:
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
'''

def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        new_matrix = []
        for each_matrix in matrix:
            new_matrix.extend(each_matrix)

        l, r = 0, len(new_matrix) - 1

        ans = self.binsearch(l, r, new_matrix, target)

        return ans >= 0

    
    def binsearch(self, l, r, nums, target):
        while l <= r:
            m = l + ((r - l) // 2)
            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = l + 1
            else:
                return m 
        return -1
