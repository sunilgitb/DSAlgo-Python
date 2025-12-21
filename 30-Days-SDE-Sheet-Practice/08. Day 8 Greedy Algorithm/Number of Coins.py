# https://leetcode.com/problems/coin-change/
# https://practice.geeksforgeeks.org/problems/number-of-coins1824/1/
# Unbounded Knapsack (Minimum coins)

import sys
from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp[i][j] = minimum coins needed to make amount j using first i coins
        dp = [[sys.maxsize] * (amount + 1) for _ in range(len(coins) + 1)]

        # Base case: amount = 0 → 0 coins needed
        for i in range(len(coins) + 1):
            dp[i][0] = 0

        # Initialize first coin row
        for j in range(1, amount + 1):
            if j % coins[0] == 0:
                dp[1][j] = j // coins[0]

        # Fill remaining dp table
        for i in range(2, len(coins) + 1):
            for j in range(1, amount + 1):
                if coins[i - 1] <= j:
                    dp[i][j] = min(
                        1 + dp[i][j - coins[i - 1]],  # take coin
                        dp[i - 1][j]                  # don't take coin
                    )
                else:
                    dp[i][j] = dp[i - 1][j]

        ans = dp[-1][-1]
        return ans if ans != sys.maxsize else -1


# ---------------- DRIVER CODE ----------------
if __name__ == "__main__":
    sol = Solution()

    coins = [1, 2, 5]
    amount = 11
    print(sol.coinChange(coins, amount))
    # Expected Output: 3   (5 + 5 + 1)

    coins = [2]
    amount = 3
    print(sol.coinChange(coins, amount))
    # Expected Output: -1

    coins = [1]
    amount = 0
    print(sol.coinChange(coins, amount))
    # Expected Output: 0
