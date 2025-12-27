# https://leetcode.com/problems/guess-number-higher-or-lower-ii/
# https://youtu.be/x--bMzT1Xhk

from typing import List
from functools import lru_cache

# Method 1: Recursive + Memoization (Top-Down DP)
class SolutionTopDown:
    def getMoneyAmount(self, n: int) -> int:
        @lru_cache(None)
        def solve(start: int, end: int) -> int:
            if start >= end:
                return 0
            min_cost = float('inf')
            for i in range(start, end):
                cost = i + max(solve(start, i - 1), solve(i + 1, end))
                min_cost = min(min_cost, cost)
            return min_cost
        
        return solve(1, n)


# Method 2: Bottom-Up DP (Most common & efficient for interviews)
class Solution:
    def getMoneyAmount(self, n: int) -> int:
        if n == 1:
            return 0
            
        # dp[i][j] = min cost to guarantee finding number in [i..j]
        dp = [[0] * (n + 2) for _ in range(n + 2)]
        
        # Fill for all lengths
        for length in range(2, n + 1):
            for start in range(1, n - length + 2):
                end = start + length - 1
                min_cost = float('inf')
                for k in range(start, end):
                    cost = k + max(dp[start][k - 1], dp[k + 1][end])
                    min_cost = min(min_cost, cost)
                dp[start][end] = min_cost
        
        return dp[1][n]


# ---------------- Example Usage ----------------
sol = Solution()

# Example 1
n = 10
print(sol.getMoneyAmount(n))  # Output: 16

# Example 2
n = 1
print(sol.getMoneyAmount(n))  # Output: 0

# Example 3
n = 2
print(sol.getMoneyAmount(n))  # Output: 1

# Example 4
n = 5
print(sol.getMoneyAmount(n))  # Output: 6

# Example 5
n = 15
print(sol.getMoneyAmount(n))  # Output: 34

# Example 6
n = 20
print(sol.getMoneyAmount(n))  # Output: 49