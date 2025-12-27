# https://www.youtube.com/watch?v=aycn9KO8_Ls&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=14
# https://practice.geeksforgeeks.org/problems/knapsack-with-duplicate-items4201/1#

class Solution:
    def knapSack(self, N, W, val, wt):
        # code here
        dp = [[0] * (W + 1) for i in range(N + 1)]
        
        # innitializing 0th row and 0th colomn = 0
        # as for zero weight profit will be zero and we are placing profit in each box
            
        for i in range(1, N + 1):
            for j in range(1, W + 1):
                if wt[i - 1] <= j:
                    dp[i][j] = max(val[i-1] + dp[i][j-wt[i-1]], dp[i-1][j])
                else:
                    dp[i][j] = dp[i-1][j]
        
        return dp[-1][-1]

# ---------------- Example Usage ----------------
sol = Solution()

# Example 1
N = 4
W = 8
val = [1, 4, 5, 7]
wt = [1, 3, 4, 5]
print(sol.knapSack(N, W, val, wt))  # Output: 11

# Example 2
N = 3
W = 4
val = [1, 4, 5]
wt = [1, 3, 4]
print(sol.knapSack(N, W, val, wt))  # Output: 5

# Example 3
N = 5
W = 10
val = [6, 8, 9, 10, 12]
wt = [2, 3, 4, 5, 6]
print(sol.knapSack(N, W, val, wt))  # Output: 24

# Example 4
N = 2
W = 3
val = [1, 1]
wt = [1, 2]
print(sol.knapSack(N, W, val, wt))  # Output: 3

# Example 5 (single item, can be used multiple times)
N = 1
W = 10
val = [10]
wt = [5]
print(sol.knapSack(N, W, val, wt))  # Output: 20

# Example 6 (classic unbounded knapsack)
N = 4
W = 7
val = [10, 40, 30, 50]
wt = [5, 4, 6, 3]
print(sol.knapSack(N, W, val, wt))  # Output: 100