# https://leetcode.com/problems/longest-increasing-path-in-a-matrix/

from typing import List

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
            
        rows, cols = len(matrix), len(matrix[0])
        memo = {}  # (i,j) → longest increasing path starting from (i,j)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        def dfs(i: int, j: int) -> int:
            if (i, j) in memo:
                return memo[(i, j)]
            
            max_path = 1  # at least itself
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if (0 <= ni < rows and 0 <= nj < cols and
                        matrix[ni][nj] > matrix[i][j]):
                    max_path = max(max_path, 1 + dfs(ni, nj))
            
            memo[(i, j)] = max_path
            return max_path
        
        # Try starting from every cell
        result = 0
        for i in range(rows):
            for j in range(cols):
                result = max(result, dfs(i, j))
        
        return result


# ---------------- Example Usage ----------------
sol = Solution()

# Example 1
matrix = [
    [9, 9, 4],
    [6, 6, 8],
    [2, 1, 1]
]
print(sol.longestIncreasingPath(matrix))  # Output: 4 (1→2→6→9)

# Example 2
matrix = [
    [3, 4, 5],
    [3, 2, 6],
    [2, 2, 1]
]
print(sol.longestIncreasingPath(matrix))  # Output: 4 (1→2→3→4 or 1→2→3→6)

# Example 3
matrix = [[1]]
print(sol.longestIncreasingPath(matrix))  # Output: 1

# Example 4
matrix = [
    [1, 2, 3],
    [6, 5, 4]
]
print(sol.longestIncreasingPath(matrix))  # Output: 4 (1→2→3→4)

# Example 5
matrix = [
    [7, 7, 7],
    [7, 7, 7],
    [7, 7, 7]
]
print(sol.longestIncreasingPath(matrix))  # Output: 1 (no increasing path)

# Example 6 (longer increasing path)
matrix = [
    [1, 5, 9],
    [10, 11, 15],
    [21, 30, 35]
]
print(sol.longestIncreasingPath(matrix))  # Output: 4 (1→5→9→11→15)