# https://practice.geeksforgeeks.org/problems/perfect-sum-problem5633/1#

class Solution:
    def perfectSum(self, arr, n, target):
        dp = [[0] * (target + 1) for _ in range(n + 1)]
        
        # Sum = 0 → one empty subset
        dp[0][0] = 1
        
        for i in range(1, n + 1):
            for j in range(target + 1):
                if arr[i - 1] <= j:
                    dp[i][j] = dp[i - 1][j] + dp[i - 1][j - arr[i - 1]]
                else:
                    dp[i][j] = dp[i - 1][j]
        
        return dp[n][target]


# Time Complexity: O(n * sum)
# Space Complexity: O(n * sum)


# ---------------- Example Usage ----------------
sol = Solution()

arr = [2, 3, 5, 6, 8, 10]
target = 10
n = len(arr)

print(sol.perfectSum(arr, n, target))
# Output: 3
