from typing import List
import sys


# Original Solution (Top-Down Memoization)
class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        dp = {}
        
        def solve(i, t):
            if t >= len(time): return 0
            if i >= len(time): return 2**31
            if (i, t) in dp: return dp[(i, t)]
            ans = min(
                solve(i + 1, t),                  # skip this painter
                cost[i] + solve(i + 1, t + time[i] + 1)  # use this painter
            )
            dp[(i, t)] = ans
            return ans
        
        return solve(0, 0)


# ========================
# Driver Code with Test Cases
# ---------------- Example Usage ----------------
sol = Solution()

# Example 1
cost = [1, 2, 3, 2]
time = [1, 2, 3, 2]
print(sol.paintWalls(cost, time))  # Output: 3

# Example 2
cost = [2, 3, 4, 2]
time = [1, 1, 1, 1]
print(sol.paintWalls(cost, time))  # Output: 4