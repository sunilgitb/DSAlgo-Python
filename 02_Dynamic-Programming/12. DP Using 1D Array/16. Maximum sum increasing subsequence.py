class Solution:
    def maxSumIS(self, arr, n):
        dp = arr.copy()  # dp[i] stores max sum of increasing subsequence ending at i
        
        for i in range(n):
            for j in range(i):
                if arr[i] > arr[j] and dp[i] < dp[j] + arr[i]:
                    dp[i] = dp[j] + arr[i]
        
        return max(dp)

# ------------------- Driver Code -------------------
if __name__ == "__main__":
    sol = Solution()
    arr = [1, 101, 2, 3, 100, 4, 5]
    n = len(arr)
    print(sol.maxSumIS(arr, n))  # Output: 106
