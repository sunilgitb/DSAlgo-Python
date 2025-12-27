# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
            
        min_so_far = prices[0]
        max_profit = 0
        
        for price in prices:
            min_so_far = min(min_so_far, price)
            profit = price - min_so_far
            max_profit = max(max_profit, profit)
        
        return max_profit


# ---------------- Example Usage ----------------
sol = Solution()

# Example 1
prices = [7, 1, 5, 3, 6, 4]
print(sol.maxProfit(prices))  # Output: 5  (buy at 1, sell at 6)

# Example 2
prices = [7, 6, 4, 3, 1]
print(sol.maxProfit(prices))  # Output: 0  (prices only decrease)

# Example 3
prices = [1]
print(sol.maxProfit(prices))  # Output: 0

# Example 4
prices = [2, 4, 1]
print(sol.maxProfit(prices))  # Output: 2  (buy at 2, sell at 4)

# Example 5
prices = [3, 2, 6, 5, 0, 3]
print(sol.maxProfit(prices))  # Output: 4  (buy at 2, sell at 6)

# Example 6
prices = [1, 2, 3, 4, 5]
print(sol.maxProfit(prices))  # Output: 4  (buy at 1, sell at 5)