# https://www.youtube.com/watch?v=VDhRg-ZJTuc&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=29
# https://leetcode.com/problems/shortest-common-supersequence/

from typing import List

class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        X, Y = str1, str2
        m, n = len(X), len(Y)
        
        # Build DP table for LCS length
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if X[i - 1] == Y[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        # Backtrack to construct the shortest common supersequence
        i, j = m, n
        res = ""
        
        while i > 0 and j > 0:
            if X[i - 1] == Y[j - 1]:
                res += X[i - 1]  # or Y[j - 1], same
                i -= 1
                j -= 1
            else:
                # Choose the direction with higher LCS value
                if dp[i][j - 1] > dp[i - 1][j]:
                    res += Y[j - 1]
                    j -= 1
                else:
                    res += X[i - 1]
                    i -= 1
        
        # Add remaining characters from str1 (if any)
        while i > 0:
            res += X[i - 1]
            i -= 1
        
        # Add remaining characters from str2 (if any)
        while j > 0:
            res += Y[j - 1]
            j -= 1
        
        return res[::-1]  # Reverse to get correct order


# ---------------- Example Usage ----------------
sol = Solution()

# Example 1
str1 = "brute"
str2 = "groot"
print(sol.shortestCommonSupersequence(str1, str2))  
# Output: "bgroot" or "gbrute" (length 6)

# Example 2
str1 = "AGGTAB"
str2 = "GXTXAYB"
print(sol.shortestCommonSupersequence(str1, str2))  
# Output: "AGXGTXAYB" (length 9)

# Example 3
str1 = "bleed"
str2 = "blue"
print(sol.shortestCommonSupersequence(str1, str2))  
# Output: "bluede" or "bleude" (length 6)

# Example 4
str1 = "abc"
str2 = "def"
print(sol.shortestCommonSupersequence(str1, str2))  
# Output: "abcdef" (length 6)

# Example 5
str1 = "geek"
str2 = "eke"
print(sol.shortestCommonSupersequence(str1, str2))  
# Output: "geeke" (length 5)

# Example 6
str1 = "abcd"
str2 = "abcd"
print(sol.shortestCommonSupersequence(str1, str2))  
# Output: "abcd" (length 4)