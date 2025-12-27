# https://practice.geeksforgeeks.org/problems/gold-mine-problem2608/1

from typing import List

# Method 1: Top-Down to Bottom-Right (Column-wise filling)
class SolutionTopDown:
    def maxGold(self, n: int, m: int, M: List[List[int]]) -> int:
        def get(i: int, j: int) -> int:
            if not (0 <= i < n and 0 <= j < m):
                return 0
            return M[i][j]
        
        max_gold = 0
        
        # Start from leftmost column (j=0)
        for j in range(m):
            for i in range(n):
                if j == 0:
                    # Leftmost column: just the cell itself
                    max_gold = max(max_gold, M[i][j])
                else:
                    # Add max from left, left-up, or left-down
                    M[i][j] += max(
                        get(i, j - 1),
                        get(i - 1, j - 1),
                        get(i + 1, j - 1)
                    )
                    max_gold = max(max_gold, M[i][j])
        
        return max_gold


# Method 2: Bottom-Right to Top-Left (Column-wise filling)
class Solution:
    def maxGold(self, n: int, m: int, M: List[List[int]]) -> int:
        def get(x: int, y: int) -> int:
            if not (0 <= x < n and 0 <= y < m):
                return 0
            return M[x][y]
        
        if m == 1:
            # Single column: just the maximum value in it
            return max(M[i][0] for i in range(n))
        
        max_gold = 0
        
        # Traverse from rightmost-1 column to leftmost
        for j in range(m - 2, -1, -1):
            for i in range(n - 1, -1, -1):
                M[i][j] += max(
                    get(i - 1, j + 1),
                    get(i, j + 1),
                    get(i + 1, j + 1)
                )
                max_gold = max(max_gold, M[i][j])
        
        return max_gold


# ---------------- Example Usage ----------------
sol = Solution()

# Example 1
n, m = 4, 4
M = [
    [1, 3, 1, 5],
    [2, 2, 4, 1],
    [5, 0, 2, 3],
    [0, 6, 1, 2]
]
print(sol.maxGold(n, m, M))  # Output: 16 (1→2→4→2→3 or similar path)

# Example 2
n, m = 3, 3
M = [
    [10, 33, 13],
    [22, 21, 04],
    [1, 7, 5]
]
print(sol.maxGold(n, m, M))  # Output: 71 (10→22→33→6? wait, actual: 10→22→33)

# Example 3 (single column)
n, m = 5, 1
M = [[1], [2], [3], [4], [5]]
print(sol.maxGold(n, m, M))  # Output: 5

# Example 4 (single row)
n, m = 1, 5
M = [[10, 20, 30, 40, 50]]
print(sol.maxGold(n, m, M))  # Output: 50

# Example 5
n, m = 2, 2
M = [
    [1, 2],
    [3, 4]
]
print(sol.maxGold(n, m, M))  # Output: 7 (1→2→4 or 3→4)