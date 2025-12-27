# https://www.youtube.com/watch?v=x5hQvnUcjiM&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=23
# https://www.geeksforgeeks.org/printing-longest-common-subsequence/

from typing import List

class Solution:
    def printLongestCommonSubsequence(self, X: str, Y: str) -> str:
        m, n = len(X), len(Y)
        
        # Build DP table (same as LCS length)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if X[i - 1] == Y[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]  # Note: diagonal + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        # Backtrack to construct the LCS string
        i, j = m, n
        res = ""
        
        while i > 0 and j > 0:
            if X[i - 1] == Y[j - 1]:
                res += X[i - 1]
                i -= 1
                j -= 1
            else:
                # Move to the direction of maximum value
                if dp[i][j - 1] > dp[i - 1][j]:
                    j -= 1
                else:
                    i -= 1
        
        return res[::-1]  # Reverse to get correct order


# ---------------- Example Usage ----------------
sol = Solution()

# Example 1 (from video/GeeksforGeeks)
X = "AGGTAB"
Y = "GXTXAYB"
print(sol.printLongestCommonSubsequence(X, Y))  # Output: "GTAB"

# Example 2
X = "ABCBDAB"
Y = "BDCAB"
print(sol.printLongestCommonSubsequence(X, Y))  # Output: "BCAB" or "BDAB" (any valid LCS)

# Example 3
X = "XMJYAUZ"
Y = "MZJAWXU"
print(sol.printLongestCommonSubsequence(X, Y))  # Output: "MJAU"

# Example 4
X = "ABCDE"
Y = "ACE"
print(sol.printLongestCommonSubsequence(X, Y))  # Output: "ACE"

# Example 5 (no common characters)
X = "abc"
Y = "def"
print(sol.printLongestCommonSubsequence(X, Y))  # Output: ""

# Example 6
X = "GeeksforGeeks"
Y = "GeeksQuiz"
print(sol.printLongestCommonSubsequence(X, Y))  # Output: "Geeks"