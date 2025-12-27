# https://leetcode.com/problems/minimum-path-sum/

from typing import List

# Method 1: Bottom-Up DP (bottom-right to top-left)
class SolutionBottomUpReverse:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
            
        rows, cols = len(grid), len(grid[0])
        
        # Fill rightmost column (only downward moves possible)
        for i in range(rows - 2, -1, -1):
            grid[i][cols - 1] += grid[i + 1][cols - 1]
        
        # Fill bottom row (only right moves possible)
        for j in range(cols - 2, -1, -1):
            grid[rows - 1][j] += grid[rows - 1][j + 1]
        
        # Fill rest of the grid
        for i in range(rows - 2, -1, -1):
            for j in range(cols - 2, -1, -1):
                grid[i][j] += min(grid[i + 1][j], grid[i][j + 1])
        
        return grid[0][0]


# Method 2: Bottom-Up DP (top-left to bottom-right) - Most common & readable
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
            
        rows, cols = len(grid), len(grid[0])
        
        # Fill first row (only right moves)
        for j in range(1, cols):
            grid[0][j] += grid[0][j - 1]
        
        # Fill first column (only down moves)
        for i in range(1, rows):
            grid[i][0] += grid[i - 1][0]
        
        # Fill rest of the grid
        for i in range(1, rows):
            for j in range(1, cols):
                grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])
        
        return grid[-1][-1]


# ---------------- Example Usage ----------------
sol = Solution()

# Example 1
grid = [
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1]
]
print(sol.minPathSum(grid))  # Output: 7 (path: 1→3→1→1→1)

# Example 2
grid = [[1,2,3],[4,5,6]]
print(sol.minPathSum(grid))  # Output: 12 (1→2→3→6 or 1→4→5→6)

# Example 3
grid = [[1,2],[1,1]]
print(sol.minPathSum(grid))  # Output: 3 (1→1→1)

# Example 4
grid = [[1]]
print(sol.minPathSum(grid))  # Output: 1

# Example 5
grid = [[1,3,1,2],[1,5,1,3],[4,2,1,1]]
print(sol.minPathSum(grid))  # Output: 8

# Example 6
grid = [[0,2,2,6,4,1,6],[0,4,0,5,0,0,4],[5,5,5,1,0,5,6]]
print(sol.minPathSum(grid))  # Output: 18