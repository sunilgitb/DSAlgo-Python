# https://www.youtube.com/watch?v=823Grn4_dCQ&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=25
# Shortest Common Supersequence Length = m + n - LCS(X, Y)

from typing import List

class Solution:
    def shortestCommonSupersequenceLength(self, X: str, Y: str) -> int:
        m, n = len(X), len(Y)
        
        # DP table for Longest Common Subsequence
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Fill DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if X[i - 1] == Y[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        LCS_length = dp[m][n]
        
        # SCS length = total characters - common (shared) characters
        return m + n - LCS_length


# ---------------- Example Usage ----------------
sol = Solution()

# Example 1 (from video)
X = "AGGTAB"
Y = "GXTXAYB"
print(sol.shortestCommonSupersequenceLength(X, Y))  
# Output: 9  (LCS = "GTAB" → length 4; 6 + 7 - 4 = 9)

# Example 2
X = "ABCBDAB"
Y = "BDCAB"
print(sol.shortestCommonSupersequenceLength(X, Y))  
# Output: 9  (LCS length = 4 → 7 + 5 - 4 = 8? Wait, correct LCS=4, answer=8)
# Correction: Actual SCS length is 8 (e.g., "ABDCBDAB")

# Example 3
X = "bleed"
Y = "blue"
print(sol.shortestCommonSupersequenceLength(X, Y))  
# Output: 6  (LCS = "ble", length 3 → 5 + 4 - 3 = 6; e.g., "blued")

# Example 4
X = "abc"
Y = "def"
print(sol.shortestCommonSupersequenceLength(X, Y))  
# Output: 6  (No common → 3 + 3 - 0 = 6)

# Example 5
X = "geek"
Y = "eke"
print(sol.shortestCommonSupersequenceLength(X, Y))  
# Output: 5  (LCS = "ek" → 4 + 3 - 2 = 5; e.g., "geeke")

# Example 6
X = "abcd"
Y = "abcd"
print(sol.shortestCommonSupersequenceLength(X, Y))  
# Output: 4  (Same strings → LCS = 4 → 4 + 4 - 4 = 4)