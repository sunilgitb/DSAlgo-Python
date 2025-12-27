# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

from typing import List

# --------------------------------------------------------------------------------------------
# 1) TOP-DOWN DP (Memoization) - Recursive with cache
# --------------------------------------------------------------------------------------------

class SolutionTopDown:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}

        def solve(i: int, can_sell: bool) -> int:
            if i == len(prices):
                return 0
            key = (i, can_sell)
            if key in memo:
                return memo[key]

            # Skip current day
            skip = solve(i + 1, can_sell)

            # Buy or Sell
            if can_sell:
                # Can sell today
                sell = prices[i] + solve(i + 1, False)
                profit = max(skip, sell)
            else:
                # Can buy today
                buy = -prices[i] + solve(i + 1, True)
                profit = max(skip, buy)

            memo[key] = profit
            return profit

        return solve(0, False)


# --------------------------------------------------------------------------------------------
# 2) BOTTOM-UP DP (Tabulation)
# --------------------------------------------------------------------------------------------

class SolutionBottomUp:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        # dp[i][0] = max profit on day i without stock (can buy)
        # dp[i][1] = max profit on day i with stock (can sell)
        dp = [[0] * 2 for _ in range(n + 1)]

        # Base case: after last day, profit is 0 regardless of state
        dp[n][0] = dp[n][1] = 0

        # Fill from last day to first
        for i in range(n - 1, -1, -1):
            for can_sell in range(2):
                # Option 1: Skip today
                skip = dp[i + 1][can_sell]

                # Option 2: Buy or Sell today
                if can_sell:
                    sell = prices[i] + dp[i + 1][0]
                    dp[i][can_sell] = max(skip, sell)
                else:
                    buy = -prices[i] + dp[i + 1][1]
                    dp[i][can_sell] = max(skip, buy)

        return dp[0][0]


# --------------------------------------------------------------------------------------------
# 3) GREEDY (Optimal & Most Efficient)
# --------------------------------------------------------------------------------------------

class SolutionGreedy:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]
        return profit


# --------------------------------------------------------------------------------------------
# DRIVER CODE & TEST CASES
# --------------------------------------------------------------------------------------------

if __name__ == "__main__":
    test_cases = [
        [7, 1, 5, 3, 6, 4],     # Expected: 7   (buy 1→sell 5, buy 3→sell 6)
        [1, 2, 3, 4, 5],       # Expected: 4   (buy 1→sell 5)
        [7, 6, 4, 3, 1],       # Expected: 0   (no profitable transaction)
        [1],                   # Expected: 0
        [2, 4, 1],             # Expected: 2   (buy 2→sell 4)
        [3, 2, 6, 5, 0, 3],    # Expected: 7   (buy 2→sell 6, buy 0→sell 3)
    ]

    print("Testing All Approaches:\n")
    for prices in test_cases:
        sol1 = SolutionTopDown()
        sol2 = SolutionBottomUp()
        sol3 = SolutionGreedy()

        p1 = sol1.maxProfit(prices)
        p2 = sol2.maxProfit(prices)
        p3 = sol3.maxProfit(prices)

        print(f"Prices: {prices}")
        print(f"Top-Down DP   : {p1}")
        print(f"Bottom-Up DP  : {p2}")
        print(f"Greedy        : {p3}")
        print("-" * 40)