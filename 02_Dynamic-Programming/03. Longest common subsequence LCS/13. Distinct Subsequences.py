# https://leetcode.com/problems/distinct-subsequences/

from typing import List

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(t), len(s)  # t is the target, s is the source
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Base case: empty string t can be formed in 1 way from any prefix of s
        for j in range(n + 1):
            dp[0][j] = 1
        
        # Fill DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # Always can skip current character in s
                dp[i][j] = dp[i][j - 1]
                
                # If characters match, add ways from previous states
                if t[i - 1] == s[j - 1]:
                    dp[i][j] += dp[i - 1][j - 1]
        
        return dp[m][n]


# ---------------- Example Usage ----------------
sol = Solution()

# Example 1
s = "rabbbit"
t = "rabbit"
print(sol.numDistinct(s, t))  # Output: 3

# Example 2
s = "babgbag"
t = "bag"
print(sol.numDistinct(s, t))  # Output: 5

# Example 3
s = "hello"
t = "lo"
print(sol.numDistinct(s, t))  # Output: 2

# Example 4
s = "abc"
t = "abc"
print(sol.numDistinct(s, t))  # Output: 1

# Example 5
s = "abc"
t = "abcc"
print(sol.numDistinct(s, t))  # Output: 0

# Example 6
s = "a"
t = "a"
print(sol.numDistinct(s, t))  # Output: 1

# Example 7
s = "aabbcc"
t = "abc"
print(sol.numDistinct(s, t))  # Output: 8