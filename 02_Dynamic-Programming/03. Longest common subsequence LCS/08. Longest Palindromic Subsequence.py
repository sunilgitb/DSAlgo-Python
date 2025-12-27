# https://www.youtube.com/watch?v=wuOOOATz_IA&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=26
# https://leetcode.com/problems/longest-palindromic-subsequence/

from typing import List

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        # Longest Palindromic Subsequence (LPS) = LCS(s, reverse(s))
        def LCS(X: str, Y: str) -> int:
            m, n = len(X), len(Y)
            dp = [[0] * (n + 1) for _ in range(m + 1)]
            
            for i in range(1, m + 1):
                for j in range(1, n + 1):
                    if X[i - 1] == Y[j - 1]:
                        dp[i][j] = 1 + dp[i - 1][j - 1]
                    else:
                        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
            
            return dp[m][n]
        
        # Return length of LCS between string and its reverse
        return LCS(s, s[::-1])


# ---------------- Example Usage ----------------
sol = Solution()

# Example 1
s = "bbbab"
print(sol.longestPalindromeSubseq(s))  # Output: 4 ("bbbb")

# Example 2
s = "cbbd"
print(sol.longestPalindromeSubseq(s))  # Output: 2 ("bb")

# Example 3
s = "agbcba"
print(sol.longestPalindromeSubseq(s))  # Output: 5 ("abcba")

# Example 4
s = "a"
print(sol.longestPalindromeSubseq(s))  # Output: 1

# Example 5
s = "character"
print(sol.longestPalindromeSubseq(s))  # Output: 5 ("carac" or similar)

# Example 6 (all distinct characters)
s = "abcde"
print(sol.longestPalindromeSubseq(s))  # Output: 1

# Example 7 (all same characters)
s = "aaaaa"
print(sol.longestPalindromeSubseq(s))  # Output: 5