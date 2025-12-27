# https://www.youtube.com/watch?v=-fx6aDxcWyg&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=25
# https://practice.geeksforgeeks.org/problems/minimum-number-of-deletions-and-insertions0209/1
# https://leetcode.com/problems/delete-operation-for-two-strings/

from typing import List

class Solution:
    def minOperations(self, s1: str, s2: str) -> int:
        X, Y = s1, s2
        m, n = len(X), len(Y)
        
        # Build DP table for Longest Common Subsequence
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if X[i - 1] == Y[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        lenOfLCS = dp[m][n]
        
        # Deletions needed = characters in s1 not in LCS
        # Insertions needed = characters in s2 not in LCS
        deletions = len(X) - lenOfLCS
        insertions = len(Y) - lenOfLCS
        
        return deletions + insertions


# ---------------- Example Usage ----------------
sol = Solution()

# Example 1 (from problem description)
s1 = "heap"
s2 = "pea"
print(sol.minOperations(s1, s2))  # Output: 3  (delete 'h','e' → "ap", insert 'p' → "pea")

# Example 2
s1 = "geeksforgeeks"
s2 = "geeks"
print(sol.minOperations(s1, s2))  # Output: 8  (delete 8 chars from s1 to keep "geeks")

# Example 3
s1 = "leetcode"
s2 = "etco"
print(sol.minOperations(s1, s2))  # Output: 4  (delete 'l','d','e' → "etco", no insertion needed)

# Example 4
s1 = "abcd"
s2 = "ac"
print(sol.minOperations(s1, s2))  # Output: 2  (delete 'b','d' → "ac")

# Example 5 (no common characters)
s1 = "abc"
s2 = "def"
print(sol.minOperations(s1, s2))  # Output: 6  (delete all 3 from s1, insert all 3 from s2)

# Example 6 (identical strings)
s1 = "hello"
s2 = "hello"
print(sol.minOperations(s1, s2))  # Output: 0  (no operations needed)