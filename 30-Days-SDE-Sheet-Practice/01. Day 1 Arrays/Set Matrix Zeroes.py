# https://leetcode.com/problems/set-matrix-zeroes/
# Approach:
'''
Instead of taking two separate dummy arrays, 
take first row and column of the matrix as the array for 
checking whether the particular column or row has the value 0 or not. 
Since matrix[0][0] are overlapping. Therefore take separate variable col0(say) to check 
if the 0th column has 0 or not and use matrix[0][0] to check if the 0th row has 0 or not. 
Now traverse from last element to the first element and check if matrix[i][0]==0 || matrix[0][j]==0 
and if true set matrix[i][j]=0, else continue.
'''
from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        col0 = 1
        
        for i in range(len(matrix)):
            if matrix[i][0] == 0:
                col0 = 0
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        for i in range(len(matrix) - 1, -1, -1):
            for j in range(len(matrix[0]) - 1, 0, -1):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
            if col0 == 0:
                matrix[i][0] = 0


# ---------------- DRIVER CODE ----------------
if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        [[1,1,1],[1,0,1],[1,1,1]],
        [[0,1,2,0],[3,4,5,2],[1,3,1,5]],
        [[1,2,3]],
        [[1],[0],[3]]
    ]

    for idx, matrix in enumerate(test_cases, 1):
        print(f"Test Case {idx}:")
        print("Before:")
        for row in matrix:
            print(row)

        sol.setZeroes(matrix)

        print("After:")
        for row in matrix:
            print(row)
        print("-" * 30)


# Time: O(N * M)
# Space: O(1)