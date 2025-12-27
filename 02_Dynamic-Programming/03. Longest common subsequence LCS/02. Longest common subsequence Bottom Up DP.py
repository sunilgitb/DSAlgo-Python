# https://www.youtube.com/watch?v=g_hIx4yn9zg&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=20
# https://leetcode.com/problems/longest-common-subsequence/

from typing import List

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        X = text1
        Y = text2
        m = len(text1)
        n = len(text2)
        
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Base case: if either string is empty, LCS length is 0
        # (already handled by initialization with 0)
        
        # Fill the dp table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if X[i - 1] == Y[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        return dp[m][n]


# ---------------- Example Usage ----------------
sol = Solution()

# Example 1
text1 = "abcde"
text2 = "ace"
print(sol.longestCommonSubsequence(text1, text2))  # Output: 3 ("ace")

# Example 2
text1 = "abc"
text2 = "abc"
print(sol.longestCommonSubsequence(text1, text2))  # Output: 3 ("abc")

# Example 3
text1 = "abc"
text2 = "def"
print(sol.longestCommonSubsequence(text1, text2))  # Output: 0

# Example 4
text1 = "ylqpejqbalahwr"
text2 = "yrkzavgdmdgtqpg"
print(sol.longestCommonSubsequence(text1, text2))  # Output: 3

# Example 5
text1 = "pmjghe"
text2 = "gpmh"
print(sol.longestCommonSubsequence(text1, text2))  # Output: 3

# Example 6
text1 = "ezupkr"
text2 = "ubmrapg"
print(sol.longestCommonSubsequence(text1, text2))  # Output: 2