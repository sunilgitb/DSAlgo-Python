# https://www.youtube.com/watch?v=I-l6PBeERuc&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=16
# https://leetcode.com/problems/coin-change/

import sys
from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # As we have infinite supply of coins so this question is a variation of Unbounded Knapsack
        dp = [[sys.maxsize] * (amount + 1) for _ in range(len(coins) + 1)]  # placing max value as we want to find minimum
        
        # Initializing 0th row = infinite; can't make any amount > 0 with 0 coins
        for j in range(amount + 1):
            dp[0][j] = sys.maxsize
        
        # 0th column: amount = 0 can be made with 0 coins (for any number of coin types)
        for i in range(1, len(coins) + 1):
            dp[i][0] = 0
        
        # *** Special handling for first coin (1st row) ***
        # For the first coin, fill only if amount is multiple of coins[0]
        for j in range(1, amount + 1):
            if j % coins[0] == 0:
                dp[1][j] = j // coins[0]
        
        # Fill remaining dp table
        for i in range(2, len(coins) + 1):
            for j in range(1, amount + 1):
                if coins[i - 1] <= j:
                    dp[i][j] = min(
                        1 + dp[i][j - coins[i - 1]],  # take this coin
                        dp[i - 1][j]                  # skip this coin
                    )
                else:
                    dp[i][j] = dp[i - 1][j]
        
        ans = dp[-1][-1]
        return ans if ans != sys.maxsize else -1


# ---------------- Example Usage ----------------
sol = Solution()

# Example 1 (LeetCode)
coins = [1, 2, 5]
amount = 11
print(sol.coinChange(coins, amount))  # Output: 3  (5 + 5 + 1)

# Example 2 (LeetCode)
coins = [2]
amount = 3
print(sol.coinChange(coins, amount))  # Output: -1

# Example 3 (LeetCode)
coins = [1]
amount = 0
print(sol.coinChange(coins, amount))  # Output: 0

# Example 4
coins = [1, 3, 4]
amount = 6
print(sol.coinChange(coins, amount))  # Output: 2  (3 + 3)

# Example 5
coins = [2, 5, 10, 1]
amount = 27
print(sol.coinChange(coins, amount))  # Output: 4  (10 + 10 + 5 + 2)

# Example 6
coins = [186, 419, 83, 408]
amount = 6249
print(sol.coinChange(coins, amount))  # Output: 20