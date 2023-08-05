'''
54. Spiral Matrix
Given:
Given an m x n matrix, return all elements of the matrix in spiral order.
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
Solution:
0) first thing is to use Left, Right, Top, Bottom pointers
1) Bottom and Right is setted to +1 offset 
2) while l < r and t < b:
    - grab all top row cells(by range(left, right)) and make top += 1
    - then grab all right col cells(by range(top, bottom) and make right -= 1, matrix[i][right -1]
    - check for l < r and t < b if one row or one col: break 
    - get the every cell in bottom row by range(right - 1, left - 1, -1): and matrix[bottom - 1][i], make bottom -= 1
    - get every cell in left col by range (bottom - 1, top - 1, -1) and matrix[i][left], make left += 1
'''
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # col++, rol++, col--, row--
        res = []
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)

        while left < right and top < bottom:
            # get every i in the top row
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1
            # get every i in the right col
            for i in range(top, bottom):
                res.append(matrix[i][right - 1])
            right -= 1
            if not (left < right and top < bottom):
                break
            # get every i in the bottom row
            for i in range(right - 1, left - 1, -1):
                res.append(matrix[bottom - 1][i])
            bottom -= 1
            # get every i in the left col
            for i in range(bottom - 1, top - 1, -1):
                res.append(matrix[i][left])
            left += 1

        return res
