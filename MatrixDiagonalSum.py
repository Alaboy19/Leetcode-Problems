'''
1572. Matrix Diagonal Sum
Given:
Given a square matrix mat, return the sum of the matrix diagonals.
Only include the sum of all the elements on the primary diagonal and all the elements on the secondary diagonal that are not part of the primary diagonal

Input: mat = [[1,2,3],
              [4,5,6],
              [7,8,9]]
Output: 25
Explanation: Diagonals sum: 1 + 5 + 9 + 3 + 7 = 25
Notice that element mat[1][1] = 5 is counted only once.

'''

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        summa = 0 
        ROW, COL = len(mat), len(mat[0])
        for i in range(ROW):
            for j in range(COL):
                if i == j:
                    summa += mat[i][j]

        for i in range(ROW):
            for j in range(COL - 1, -1, -1):
                if not (i == ROW // 2 and j == COL // 2 and ROW % 2 == 1) and (abs(i) + abs(j) == ROW -1):
                    summa += mat[i][j]

        return summa
