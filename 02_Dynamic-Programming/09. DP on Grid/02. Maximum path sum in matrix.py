# https://practice.geeksforgeeks.org/problems/path-in-matrix3805/1

from typing import List

# Method 1: Bottom-Up DP (bottom-right to top-left)
class SolutionBottomUpReverse:
    def maximumPath(self, N: int, Matrix: List[List[int]]) -> int:
        if N == 0:
            return 0
        
        # If only one row, maximum path is just the maximum element in that row
        if N == 1:
            return max(Matrix[0])
        
        res = 0
        
        # Fill from second-last row to first row
        for i in range(N - 2, -1, -1):
            for j in range(N):
                down = Matrix[i + 1][j] if 0 <= j < N else 0
                down_left = Matrix[i + 1][j - 1] if 0 <= j - 1 < N else 0
                down_right = Matrix[i + 1][j + 1] if 0 <= j + 1 < N else 0
                
                Matrix[i][j] += max(down, down_left, down_right)
                res = max(res, Matrix[i][j])
        
        return res


# Method 2: Bottom-Up DP (top-left to bottom-right) - Most common & readable
class Solution:
    def maximumPath(self, N: int, Matrix: List[List[int]]) -> int:
        if N == 0:
            return 0
        
        res = max(Matrix[0])  # max in first row (base case)
        
        for i in range(1, N):
            for j in range(N):
                candidates = []
                
                # From above
                candidates.append(Matrix[i - 1][j])
                
                # From above-left
                if j > 0:
                    candidates.append(Matrix[i - 1][j - 1])
                
                # From above-right
                if j < N - 1:
                    candidates.append(Matrix[i - 1][j + 1])
                
                Matrix[i][j] += max(candidates)
                res = max(res, Matrix[i][j])
        
        return res


# ---------------- Example Usage ----------------
sol = Solution()

# Example 1
N = 3
Matrix = [
    [1, 2, 3],
    [4, 8, 2],
    [1, 5, 3]
]
print(sol.maximumPath(N, Matrix))  # Output: 14 (1 → 8 → 5)

# Example 2
N = 4
Matrix = [
    [3, 2, 1, 4],
    [1, 5, 3, 2],
    [6, 4, 7, 5],
    [9, 8, 2, 1]
]
print(sol.maximumPath(N, Matrix))  # Output: 25

# Example 3 (single row)
N = 1
Matrix = [[5, 10, 15]]
print(sol.maximumPath(N, Matrix))  # Output: 15

# Example 4
N = 2
Matrix = [
    [1, 2],
    [3, 4]
]
print(sol.maximumPath(N, Matrix))  # Output: 7 (1 → 2 → 4 or 3 → 4)

# Example 5
N = 5
Matrix = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
]
print(sol.maximumPath(N, Matrix))  # Output: 75 (zigzag path maximizing sum)