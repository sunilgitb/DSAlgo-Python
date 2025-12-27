# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/

from typing import List

# Memoized Top-Down DP (Recursive)
class SolutionMemo:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        memo = {}

        def solve(i: int, can_sell: bool) -> int:
            if i == n:
                return 0
            key = (i, can_sell)
            if key in memo:
                return memo[key]

            # Skip current day
            skip = solve(i + 1, can_sell)

            # Buy or Sell
            if can_sell:
                sell = prices[i] - fee + solve(i + 1, False)
                profit = max(skip, sell)
            else:
                buy = -prices[i] + solve(i + 1, True)
                profit = max(skip, buy)

            memo[key] = profit
            return profit

        return solve(0, False)


# Bottom-Up DP (Tabulation) - Space-Optimized
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        # dp[i][0] = max profit on day i without stock (can buy)
        # dp[i][1] = max profit on day i with stock (can sell)
        dp = [[0] * 2 for _ in range(n + 1)]

        # Base case: after last day, profit is 0
        dp[n][0] = dp[n][1] = 0

        # Fill from last day to first
        for i in range(n - 1, -1, -1):
            for can_sell in range(2):
                # Option 1: Skip today
                skip = dp[i + 1][can_sell]

                # Option 2: Buy or Sell today
                if can_sell:
                    sell = prices[i] - fee + dp[i + 1][0]
                    dp[i][can_sell] = max(skip, sell)
                else:
                    buy = -prices[i] + dp[i + 1][1]
                    dp[i][can_sell] = max(skip, buy)

        return dp[0][0]


# Greedy (Most Efficient)
class SolutionGreedy:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        profit = 0
        min_buy = prices[0]

        for i in range(1, len(prices)):
            # Update minimum buy price
            min_buy = min(min_buy, prices[i])

            # If selling today is profitable after fee
            if prices[i] - min_buy > fee:
                profit += prices[i] - min_buy - fee
                min_buy = prices[i]  # reset buy price after selling

        return profit


# ---------------- Example Usage ----------------
sol = Solution()

# Example 1
prices = [1, 3, 2, 8, 4, 9]
fee = 2
print(sol.maxProfit(prices, fee))  # Output: 8  (buy 1→sell 8, buy 4→sell 9)

# Example 2
prices = [1, 3, 7, 5, 10, 3]
fee = 3
print(sol.maxProfit(prices, fee))  # Output: 6  (buy 1→sell 7, buy 3→sell 10)

# Example 3
prices = [1, 2, 3, 4, 5]
fee = 1
print(sol.maxProfit(prices, fee))  # Output: 4  (buy 1→sell 5)

# Example 4
prices = [7, 6, 4, 3, 1]
fee = 2
print(sol.maxProfit(prices, fee))  # Output: 0

# Example 5
prices = [1, 3, 2, 8, 4, 9]
fee = 5
print(sol.maxProfit(prices, fee))  # Output: 4  (buy 1→sell 8, fee too high for second trade)