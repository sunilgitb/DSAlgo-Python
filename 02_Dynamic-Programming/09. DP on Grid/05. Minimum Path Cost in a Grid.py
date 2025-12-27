# https://leetcode.com/problems/minimum-path-cost-in-a-grid/

from typing import List
import copy

class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        
        # dp[i][j] = min cost to reach cell (i,j) from top row
        dp = [[0] * cols for _ in range(rows)]
        
        # Initialize first row
        for j in range(cols):
            dp[0][j] = grid[0][j]
        
        # Fill dp for each subsequent row
        for i in range(1, rows):
            for j in range(cols):
                min_cost = float('inf')
                # Try coming from every possible cell in the previous row
                for k in range(cols):
                    cost = dp[i-1][k] + moveCost[grid[i-1][k]][j]
                    min_cost = min(min_cost, cost)
                dp[i][j] = grid[i][j] + min_cost
        
        # Minimum cost to reach any cell in the last row
        return min(dp[-1])


# ---------------- Example Usage ----------------
sol = Solution()

# Example 1
grid = [[5,3],[4,0],[2,1]]
moveCost = [[9,8],[1,5],[10,12],[18,6],[2,4],[14,3]]
print(sol.minPathCost(grid, moveCost))  # Output: 17

# Example 2
grid = [[5,1,2],[4,0,3]]
moveCost = [[12,10,15],[20,23,8],[21,18,5]]
print(sol.minPathCost(grid, moveCost))  # Output: 6

# Example 3
grid = [[0]]
moveCost = [[0]*9 for _ in range(9)]  # irrelevant
print(sol.minPathCost(grid, moveCost))  # Output: 0

# Example 4 (larger grid)
grid = [[1,2,3],[4,5,6],[7,8,9]]
moveCost = [[1]*9 for _ in range(9)]  # small move costs
print(sol.minPathCost(grid, moveCost))  # Output: 10 (1→4→7→8→9 or similar)

# Example 5
grid = [[1,10],[10,1]]
moveCost = [[0]*9 for _ in range(9)]
print(sol.minPathCost(grid, moveCost))  # Output: 2 (1→10→1)