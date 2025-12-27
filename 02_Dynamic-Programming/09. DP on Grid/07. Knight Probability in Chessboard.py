# https://leetcode.com/problems/knight-probability-in-chessboard/

from typing import List, Tuple

class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        # Knight's 8 possible moves
        moves = [
            [-2, -1], [-2, 1], [2, -1], [2, 1],
            [-1, -2], [-1, 2], [1, -2], [1, 2]
        ]
        
        # Memoization table: (row, col, remaining moves) → probability
        memo = {}
        
        def dfs(r: int, c: int, remaining: int) -> float:
            # Base case: no more moves → probability 1 (still on board)
            if remaining == 0:
                return 1.0
            
            key = (r, c, remaining)
            if key in memo:
                return memo[key]
            
            prob = 0.0
            for dr, dc in moves:
                nr, nc = r + dr, c + dc
                # If next position is on the board
                if 0 <= nr < n and 0 <= nc < n:
                    prob += dfs(nr, nc, remaining - 1)
            
            # Each move has 1/8 probability
            memo[key] = prob / 8.0
            return memo[key]
        
        return dfs(row, column, k)


# ---------------- Example Usage ----------------
sol = Solution()

# Example 1
n = 3
k = 2
row = 0
column = 0
print(sol.knightProbability(n, k, row, column))  # Output: 0.06250

# Example 2
n = 1
k = 0
row = 0
column = 0
print(sol.knightProbability(n, k, row, column))  # Output: 1.00000

# Example 3
n = 8
k = 30
row = 6
column = 4
print(sol.knightProbability(n, k, row, column))  # Output: 0.00000 (very small number)

# Example 4
n = 3
k = 1
row = 1
column = 1
print(sol.knightProbability(n, k, row, column))  # Output: 0.37500

# Example 5
n = 6
k = 5
row = 2
column = 3
print(sol.knightProbability(n, k, row, column))  # Output: ~0.90625