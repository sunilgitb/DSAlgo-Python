from typing import List

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        travel_days = set(days)
        last_day = days[-1]
        
        dp = [0] * (last_day + 1)
        
        for i in range(1, last_day + 1):
            if i not in travel_days:
                dp[i] = dp[i - 1]
            else:
                cost1 = dp[i - 1] + costs[0]
                cost7 = dp[max(0, i - 7)] + costs[1]
                cost30 = dp[max(0, i - 30)] + costs[2]
                
                dp[i] = min(cost1, cost7, cost30)
        
        return dp[last_day]


# ---------------- Example Usage ----------------
if __name__ == "__main__":
    sol = Solution()
    
    days = [1, 4, 6, 7, 8, 20]
    costs = [2, 7, 15]
    
    print(sol.mincostTickets(days, costs))
    # Output: 11
