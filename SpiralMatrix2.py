'''
59. Spiral Matrix II
Given:
Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.
Input: n = 3
Output: [[1,2,3],[8,9,4],[7,6,5]]
Solution:
0) the idea is the same as in spiral matrix, to track left, right, top, bottom pointers
1) bottom and right pointer is offseted by one
1.1) by while loop with l<r and t < b and for loop for each of the following, 2-5
2) assign topest row and top += 1
3) assign rightest col and right -=1
4) assign bottom row and bottom -= 1
5) assign leftest col and left += 1
6) then it will chop off outer layer, then co inside square 
7) it is done by while loop with l<r and t < b
'''
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[None for i in range(n)] for i in range(n)]
        left, right = 0, n
        top, bottom = 0, n

        nums = list(range(n*n, 0, -1))

        while left < right and top < bottom:
            # get every i in the top row
            for i in range(left, right):
                matrix[top][i] = nums.pop()
            top += 1
            # get every i in the right col
            for i in range(top, bottom):
                matrix[i][right - 1] = nums.pop()
            right -= 1
            if not (left < right and top < bottom):
                break
            # get every i in the bottom row
            for i in range(right - 1, left - 1, -1):
                matrix[bottom - 1][i] = nums.pop()
            bottom -= 1
            # get every i in the left col
            for i in range(bottom - 1, top - 1, -1):
                matrix[i][left] = nums.pop()
            left += 1

        return matrix
