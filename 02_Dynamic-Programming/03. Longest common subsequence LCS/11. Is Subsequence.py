# https://www.youtube.com/watch?v=QVntmksK2es&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=30
# https://leetcode.com/problems/is-subsequence/
# https://practice.geeksforgeeks.org/problems/check-for-subsequence4930/1

from typing import List

# DP Approach (LCS based)
class SolutionDP:
    def isSubsequence(self, s: str, t: str) -> bool:
        m, n = len(s), len(t)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
        
        return dp[m][n] == m


# Optimal Two-Pointer Approach (Best for interviews)
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = j = 0  # i for s, j for t
        
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        
        return i == len(s)


# ---------------- Example Usage ----------------
sol = Solution()

# Example 1 (LeetCode)
s = "abc"
t = "ahbgdc"
print(sol.isSubsequence(s, t))  # Output: True

# Example 2
s = "axc"
t = "ahbgdc"
print(sol.isSubsequence(s, t))  # Output: False

# Example 3
s = ""
t = "anything"
print(sol.isSubsequence(s, t))  # Output: True (empty string is subsequence of any string)

# Example 4
s = "aaaaaa"
t = "bbaaaa"
print(sol.isSubsequence(s, t))  # Output: True

# Example 5
s = "abcd"
t = "abc"
print(sol.isSubsequence(s, t))  # Output: False

# Example 6
s = "ace"
t = "abcde"
print(sol.isSubsequence(s, t))  # Output: True