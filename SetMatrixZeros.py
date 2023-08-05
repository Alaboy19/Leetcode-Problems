'''
73. Set Matrix Zeroes
Given:
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
You must do it in place.
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
Solution:
0) init two sets with i and j that crosses zero
1) fill zero_i, zero_j sets 
2) then iterate on them and fill every cell that aligns with these beams -> make zero
Time complexity - > O(m * n)
Space Complexity -> O(m + n)
'''
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zero_i = set()
        zero_j = set()

        rows, cols = len(matrix), len(matrix[0])

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    zero_i.add(i)
                    zero_j.add(j)

        for i in zero_i:
            for j in range(cols):
                matrix[i][j] = 0

        for j in zero_j:
            for i in range(rows):
                matrix[i][j] = 0 
