# https://leetcode.com/problems/perfect-squares/

import math
from typing import List

# 2D DP Approach (similar to Coin Change with squares as coins)
class Solution2D:
    def numSquares(self, n: int) -> int:
        row = int(math.sqrt(n)) + 1
        dp = [[2**31] * (n + 1) for _ in range(row)]
        
        for i in range(row):
            dp[i][0] = 0
        
        for i in range(1, row):
            for j in range(1, n + 1):
                if i**2 <= j:
                    dp[i][j] = min(dp[i - 1][j], 1 + dp[i][j - i**2])
                else:
                    dp[i][j] = dp[i - 1][j]
        
        return dp[-1][-1]


# 1D DP Optimized Approach (Most common & efficient)
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [n] * (n + 1)
        dp[0] = 0
        
        for i in range(1, n + 1):
            for s in range(1, int(math.sqrt(i)) + 1):
                sq = s * s
                if sq > i:
                    break
                dp[i] = min(dp[i], 1 + dp[i - sq])
        
        return dp[n]


# ---------------- Example Usage ----------------
sol = Solution()

# Example 1
n = 12
print(sol.numSquares(n))  # Output: 3  (4 + 4 + 4)

# Example 2
n = 13
print(sol.numSquares(n))  # Output: 2  (4 + 9)

# Example 3
n = 1
print(sol.numSquares(n))  # Output: 1

# Example 4
n = 0
print(sol.numSquares(n))  # Output: 0

# Example 5
n = 4
print(sol.numSquares(n))  # Output: 1  (2^2)

# Example 6
n = 27
print(sol.numSquares(n))  # Output: 3  (9 + 9 + 9)

# Example 7 (large value)
n = 100
print(sol.numSquares(n))  # Output: 1  (10^2)