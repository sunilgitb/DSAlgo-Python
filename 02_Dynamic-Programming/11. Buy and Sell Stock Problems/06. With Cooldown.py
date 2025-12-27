# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        def solve(i, can_sell):
            if i >= len(prices): return 0
            if (i,can_sell) in memo: return memo[(i,can_sell)]
            if can_sell == 1: 
                profit = max(prices[i] + solve(i+2,0), solve(i+1,1))    # After selling cooldown one day
            else:
                profit = max(-prices[i] + solve(i+1,1), solve(i+1,0))
            memo[(i,can_sell)] = profit
            return profit
        return solve(0,0)
    
# Time: O(2 * N)
# Space: O(2 * N)
sol = Solution()

print(sol.maxProfit([1,2,3,0,2]))
# Expected Output: 3
# Explanation:
# Buy on day 0 (price = 1)
# Sell on day 2 (price = 3)
# Cooldown day 3
# Buy on day 3 (price = 0)
# Sell on day 4 (price = 2)

print(sol.maxProfit([1]))
# Expected Output: 0

print(sol.maxProfit([2,1,4]))
# Expected Output: 3

