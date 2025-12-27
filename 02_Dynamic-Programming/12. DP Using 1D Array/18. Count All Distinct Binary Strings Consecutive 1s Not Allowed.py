class Solution:
    def countStrings(self, n):
        mod = 10**9 + 7
        if n == 1: 
            return 2
        if n == 2:
            return 3
        
        dp = [0]*n
        dp[0] = 2
        dp[1] = 3
        
        for i in range(2, n):
            dp[i] = (dp[i-1] + dp[i-2]) % mod
        
        return dp[-1]

# ------------------- Driver Code -------------------
if __name__ == "__main__":
    sol = Solution()
    n = 5
    print(sol.countStrings(n))  # Output: 13
