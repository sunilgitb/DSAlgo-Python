# https://leetcode.com/problems/count-number-of-ways-to-place-houses/

from typing import List

# Optimized Solution (O(n) time, O(1) space)
class Solution:
    def countHousePlacements(self, n: int) -> int:
        MOD = 10**9 + 7
        a, b = 1, 1  # ways for 0 houses, 1 house
        
        for _ in range(n):
            a, b = b, (a + b) % MOD
        
        # Total ways = (ways on one side) × (ways on the other side)
        return (b * b) % MOD


# DP Array Version (O(n) time, O(n) space)
class SolutionDP:
    def countHousePlacements(self, n: int) -> int:
        MOD = 10**9 + 7
        if n == 0:
            return 1
        
        dp = [0] * (n + 2)
        dp[0] = 1  # 0 houses
        dp[1] = 1  # 1 house
        
        for i in range(2, n + 2):
            dp[i] = (dp[i-1] + dp[i-2]) % MOD
        
        return (dp[n+1] * dp[n+1]) % MOD


# ---------------- Example Usage ----------------
sol = Solution()

# Example 1
n = 1
print(sol.countHousePlacements(n))  # Output: 4
# Possibilities: [empty, house] × [empty, house] = 2 × 2 = 4

# Example 2
n = 2
print(sol.countHousePlacements(n))  # Output: 9

# Example 3
n = 3
print(sol.countHousePlacements(n))  # Output: 25

# Example 4
n = 4
print(sol.countHousePlacements(n))  # Output: 64

# Example 5
n = 0
print(sol.countHousePlacements(n))  # Output: 1 (both sides empty)

# Example 6 (large n)
n = 10
print(sol.countHousePlacements(n))  # Output: 35721