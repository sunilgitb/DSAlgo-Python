# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/

from typing import List

# Method 1: DP with Memoization (Top-Down) - General & Flexible
class SolutionTopDown:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        memo = {}

        def solve(i: int, k: int, can_sell: bool) -> int:
            if i == n or k == 0:
                return 0
            key = (i, k, can_sell)
            if key in memo:
                return memo[key]

            # Skip current day
            skip = solve(i + 1, k, can_sell)

            # Buy or Sell
            if can_sell:
                sell = prices[i] + solve(i + 1, k - 1, False)
                profit = max(skip, sell)
            else:
                buy = -prices[i] + solve(i + 1, k, True)
                profit = max(skip, buy)

            memo[key] = profit
            return profit

        return solve(0, 2, False)


# Method 2: Optimized O(n) Space & Time (Best for Interviews)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n < 2:
            return 0

        # profit1[i] = max profit using at most 1 transaction in [0..i]
        profit1 = [0] * n
        min_price = prices[0]
        for i in range(1, n):
            profit1[i] = max(profit1[i - 1], prices[i] - min_price)
            min_price = min(min_price, prices[i])

        # profit2[i] = max profit using at most 1 transaction in [i..n-1]
        profit2 = [0] * n
        max_price = prices[-1]
        for i in range(n - 2, -1, -1):
            profit2[i] = max(profit2[i + 1], max_price - prices[i])
            max_price = max(max_price, prices[i])

        # Best split: max(profit1[i] + profit2[i+1])
        max_profit = 0
        for i in range(n - 1):
            max_profit = max(max_profit, profit1[i] + profit2[i + 1])

        return max_profit


# ---------------- Example Usage ----------------
sol = Solution()

# Example 1
prices = [3, 3, 5, 0, 0, 3, 1, 4]
print(sol.maxProfit(prices))  # Output: 6  (buy 3→sell 5, buy 0→sell 4)

# Example 2
prices = [1, 2, 3, 4, 5]
print(sol.maxProfit(prices))  # Output: 4  (buy 1→sell 5)

# Example 3
prices = [7, 6, 4, 3, 1]
print(sol.maxProfit(prices))  # Output: 0  (no profitable transaction)

# Example 4
prices = [1, 2, 4, 2, 5, 7, 2, 4, 9, 3]
print(sol.maxProfit(prices))  # Output: 12 (buy 1→sell 4, buy 2→sell 9)

# Example 5
prices = [2, 1, 4, 5, 2, 9, 7]
print(sol.maxProfit(prices))  # Output: 10 (buy 1→sell 5, buy 2→sell 9)

# Example 6 (single transaction max)
prices = [7, 1, 5, 3, 6, 4]
print(sol.maxProfit(prices))  # Output: 5  (same as single transaction case)