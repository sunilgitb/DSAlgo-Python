# https://www.youtube.com/watch?v=HrybPYpOvz0&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=22
# https://practice.geeksforgeeks.org/problems/longest-common-substring1452/1#

from typing import List

class Solution:
    def longestCommonSubstr(self, S1: str, S2: str, n: int, m: int) -> int:
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        res = 0
        
        # Build DP table
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if S1[i - 1] == S2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                    res = max(res, dp[i][j])
                else:
                    dp[i][j] = 0
        
        return res


# ---------------- Example Usage ----------------
sol = Solution()

# Example 1
S1 = "ABCDGH"
S2 = "ACDGHR"
n = len(S1)
m = len(S2)
print(sol.longestCommonSubstr(S1, S2, n, m))  # Output: 4 ("CDGH")

# Example 2
S1 = "ABC"
S2 = "ACB"
n = len(S1)
m = len(S2)
print(sol.longestCommonSubstr(S1, S2, n, m))  # Output: 2 ("AB" or "AC" or "CB")

# Example 3
S1 = "AGGTAB"
S2 = "GXTXAYB"
n = len(S1)
m = len(S2)
print(sol.longestCommonSubstr(S1, S2, n, m))  # Output: 4 ("GTAB")

# Example 4
S1 = "abcdxyz"
S2 = "xyzabcd"
n = len(S1)
m = len(S2)
print(sol.longestCommonSubstr(S1, S2, n, m))  # Output: 4 ("abcd" or "xyz")

# Example 5
S1 = "GeeksforGeeks"
S2 = "GeeksQuiz"
n = len(S1)
m = len(S2)
print(sol.longestCommonSubstr(S1, S2, n, m))  # Output: 5 ("Geeks")

# Example 6 (no common substring)
S1 = "abc"
S2 = "def"
n = len(S1)
m = len(S2)
print(sol.longestCommonSubstr(S1, S2, n, m))  # Output: 0