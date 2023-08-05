'''
48. Rotate Image
Given:
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]
Solution:
0) the idea is to swap by circular loops 
1) the first thing is to remember the first -> temp, then second -> first, third -> second, fourth -> third, temp -> fourth in swap function, use for loop for each layer in range (R-L)
2) then find out how L,R,T,B is shifted by one  in range of R - L 
3) one one outer layer is done
        L, R = L + 1, R - 1
        T, B = T + 1, B - 1 to go another layer, do do while L < R
'''
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        def swap(matrix: List[List[int]], L, R) -> None:
            diff = R - L
            for i in range(diff):
                temp = matrix[T + i][L]
                matrix[T + i][L] = matrix[B][L + i]
                matrix[B][L + i] = matrix[B - i][R]
                matrix[B - i][R] = matrix[T][R - i]
                matrix[T][R - i] = temp 



        rows, cols = len(matrix) - 1, len(matrix[0]) - 1
        L, R = 0, cols
        T, B = 0, rows

        while L < R and T < B:
            swap(matrix,L, R)
            L, R = L + 1, R - 1
            T, B = T + 1, B - 1
