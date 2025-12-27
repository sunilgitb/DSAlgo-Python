# https://www.youtube.com/watch?v=hbTaCmQGqLg&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=29
# https://practice.geeksforgeeks.org/problems/longest-repeating-subsequence2004/1

from typing import List

class Solution:
    def LongestRepeatingSubsequence(self, str: str) -> int:
        X = str
        Y = str
        n = m = len(str)
        
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Fill DP table with special condition for repeating subsequence
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if X[i - 1] == Y[j - 1] and i != j:  # Characters match AND different indices
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        return dp[m][n]


# ---------------- Example Usage ----------------
sol = Solution()

# Example 1
str = "aab"
print(sol.LongestRepeatingSubsequence(str))  # Output: 1 ("a")

# Example 2
str = "axxxy"
print(sol.LongestRepeatingSubsequence(str))  # Output: 2 ("xx")

# Example 3
str = "abcd"
print(sol.LongestRepeatingSubsequence(str))  # Output: 0 (no repeating subsequence)

# Example 4
str = "aabbcc"
print(sol.LongestRepeatingSubsequence(str))  # Output: 3 ("abc")

# Example 5
str = "geeksforgeeks"
print(sol.LongestRepeatingSubsequence(str))  # Output: 6 ("eeks" or "geeks")

# Example 6
str = "aaa"
print(sol.LongestRepeatingSubsequence(str))  # Output: 2 ("aa")

# Example 7
str = "abcabc"
print(sol.LongestRepeatingSubsequence(str))  # Output: 3 ("abc")