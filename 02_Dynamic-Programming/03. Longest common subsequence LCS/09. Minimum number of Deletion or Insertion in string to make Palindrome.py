# https://www.youtube.com/watch?v=CFwCCNbRuLY&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=27
# https://practice.geeksforgeeks.org/problems/minimum-deletitions1648/1#
# https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/

from typing import List

class Solution:
    def minimumNumberOfDeletions(self, S: str) -> int:
        # Minimum deletions to make string a palindrome = len(S) - LPS(S)
        # Where LPS(S) = Longest Palindromic Subsequence = LCS(S, reverse(S))
        
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
        
        LPS_length = LCS(S, S[::-1])
        return len(S) - LPS_length


# ---------------- Example Usage ----------------
sol = Solution()

# Example 1
S = "aebcbda"
print(sol.minimumNumberOfDeletions(S))  # Output: 2  (delete 'e' and 'd' → "abcba")

# Example 2
S = "geeksforgeeks"
print(sol.minimumNumberOfDeletions(S))  # Output: 8  (keep "geekskeeg" or similar → length 5)

# Example 3
S = "bbbab"
print(sol.minimumNumberOfDeletions(S))  # Output: 1  (delete one 'b' → "bbbb")

# Example 4
S = "abcd"
print(sol.minimumNumberOfDeletions(S))  # Output: 3  (keep one character)

# Example 5
S = "aaaba"
print(sol.minimumNumberOfDeletions(S))  # Output: 1  (delete one 'b' → "aaaa")

# Example 6
S = "racecar"
print(sol.minimumNumberOfDeletions(S))  # Output: 0  (already palindrome)

# Example 7 (LeetCode min insertions equivalent)
S = "mbadm"
print(sol.minimumNumberOfDeletions(S))  # Output: 2  (insertions: "mbdadm" → "mbdadbm" or similar)