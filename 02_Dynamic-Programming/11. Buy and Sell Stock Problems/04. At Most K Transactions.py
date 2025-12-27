# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/

from typing import List

# Optimized DP Solution (O(n*k) time, O(n) space)
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        if n <= 1 or k == 0:
            return 0
        
        # If k is large enough, we can perform unlimited transactions
        if k >= n // 2:
            profit = 0
            for i in range(1, n):
                if prices[i] > prices[i - 1]:
                    profit += prices[i] - prices[i - 1]
            return profit
        
        # dp[t][d] = max profit using at most t transactions up to day d
        dp = [[0] * n for _ in range(k + 1)]
        
        for t in range(1, k + 1):
            max_diff = float('-inf')  # max(dp[t-1][prev] - prices[prev])
            for d in range(1, n):
                # Update max_diff with the best previous buy
                max_diff = max(max_diff, dp[t - 1][d - 1] - prices[d - 1])
                # Either skip today or sell today
                dp[t][d] = max(dp[t][d - 1], prices[d] + max_diff)
        
        return dp[k][n - 1]


# ---------------- Example Usage ----------------
sol = Solution()

# Example 1
k = 2
prices = [2, 4, 1]
print(sol.maxProfit(k, prices))  # Output: 2

# Example 2
k = 2
prices = [3, 2, 6, 5, 0, 3]
print(sol.maxProfit(k, prices))  # Output: 7

# Example 3
k = 2
prices = [3, 3, 5, 0, 0, 3, 1, 4]
print(sol.maxProfit(k, prices))  # Output: 6

# Example 4
k = 3
prices = [1, 2, 3, 4, 5]
print(sol.maxProfit(k, prices))  # Output: 4

# Example 5
k = 100
prices = [7, 6, 4, 3, 1]
print(sol.maxProfit(k, prices))  # Output: 0

# Example 6
k = 2
prices = [1, 2, 4, 2, 5, 7, 2, 4, 9, 3]
print(sol.maxProfit(k, prices))  # Output: 12