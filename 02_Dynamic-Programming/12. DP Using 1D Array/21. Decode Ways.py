from typing import List

# ---------------- Memoization (Top-down) ----------------
class SolutionMemo:
    def numDecodings(self, s: str) -> int:
        memo = {}
        
        def dfs(sub: str) -> int:
            if not sub:  # empty string -> valid decoding
                return 1
            if sub[0] == "0":  # leading 0 is invalid
                return 0
            if sub in memo:
                return memo[sub]
            
            # Take 1 digit
            ans = dfs(sub[1:])
            # Take 2 digits if <= 26
            if len(sub) >= 2 and int(sub[:2]) <= 26:
                ans += dfs(sub[2:])
            
            memo[sub] = ans
            return ans
        
        return dfs(s)

# ---------------- DP (Bottom-up) ----------------
class SolutionDP:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n + 1)
        dp[n] = 1  # base case: empty string
        
        for i in range(n - 1, -1, -1):
            if s[i] != '0':  # Single digit decoding
                dp[i] = dp[i + 1]
            if i + 1 < n and (s[i] == '1' or (s[i] == '2' and s[i+1] <= '6')):  # Two-digit decoding
                dp[i] += dp[i + 2]
        
        return dp[0]

# ------------------- Driver Code -------------------
if __name__ == "__main__":
    s = "226"
    
    sol_memo = SolutionMemo()
    print(sol_memo.numDecodings(s))  # Output: 3
    
    sol_dp = SolutionDP()
    print(sol_dp.numDecodings(s))    # Output: 3
