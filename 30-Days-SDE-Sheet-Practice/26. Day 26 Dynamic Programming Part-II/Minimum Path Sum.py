# https://leetcode.com/problems/minimum-path-sum/

from typing import List
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        r = len(grid)
        c = len(grid[0])
        
        for i in range(r):
            for j in range(c):
                if i == j == 0: continue
                    
                elif i == 0: grid[i][j] += grid[i][j-1]
                    
                elif j == 0: grid[i][j] += grid[i-1][j]
                    
                else: grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        
        return grid[-1][-1]
    
        
# Example Usage:
solution = Solution()
grid = [[1,3,1],[1,5,1],[4,2,1]]
print(solution.minPathSum(grid))  # Output: 7


class Solution:
    def minPathSum(self, grid):
        # Bottom-Right to Top-Left Traversal

        r = len(grid);  c = len(grid[0])
        for i in range(r-1, -1, -1):
            for j in range(c-1, -1, -1):
                
                if i == r-1 and j < c-1:
                    grid[i][j] += grid[i][j+1]
                    
                elif i < r-1 and j == c-1:
                    grid[i][j] += grid[i+1][j]
                    
                elif i < r-1 and j < c-1:
                    grid[i][j] += min(grid[i+1][j], grid[i][j+1])
        
        return grid[0][0]
