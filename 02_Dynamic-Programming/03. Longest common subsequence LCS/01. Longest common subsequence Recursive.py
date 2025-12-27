# https://www.youtube.com/watch?v=4Urd0a0BNng&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=20
# https://leetcode.com/problems/longest-common-subsequence/

from typing import List

# Recursive Approach (will TLE on large inputs)
class SolutionRecursive:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        X, Y = text1, text2
        n, m = len(X), len(Y)
        
        def LCS(X, Y, n, m):
            if n == 0 or m == 0:
                return 0
            if X[n - 1] == Y[m - 1]:
                return 1 + LCS(X, Y, n - 1, m - 1)
            else:
                return max(LCS(X, Y, n - 1, m), LCS(X, Y, n, m - 1))
        
        return LCS(X, Y, n, m)


# Memoized Top-Down DP (Efficient)
class SolutionMemo:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n, m = len(text1), len(text2)
        dp = [[-1] * (m + 1) for _ in range(n + 1)]
        
        def LCS(i: int, j: int) -> int:
            if i == 0 or j == 0:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = 1 + LCS(i - 1, j - 1)
            else:
                dp[i][j] = max(LCS(i - 1, j), LCS(i, j - 1))
            
            return dp[i][j]
        
        return LCS(n, m)


# Bottom-Up DP (Most common & efficient for interviews)
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n, m = len(text1), len(text2)
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        return dp[n][m]


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

# Example 4 (large input that causes TLE in recursive)
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