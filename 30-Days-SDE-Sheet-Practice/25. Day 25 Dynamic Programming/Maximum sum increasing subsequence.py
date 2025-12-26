# https://practice.geeksforgeeks.org/problems/maximum-sum-increasing-subsequence4749/1#

class Solution:
    def maxSumIS(self, arr, n):
        # dp[i] = maximum sum of increasing subsequence ending at index i
        dp = arr.copy()

        for i in range(n):
            for j in range(i):
                if arr[i] > arr[j]:
                    dp[i] = max(dp[i], dp[j] + arr[i])

        return max(dp)
        

# Time Complexity: O(n^2)
# Space Complexity: O(n)

# Example Usage:
sol = Solution()
arr = [1, 101, 2, 3, 100, 4, 5]
n = len(arr)
print(sol.maxSumIS(arr, n))  # Output: 106
