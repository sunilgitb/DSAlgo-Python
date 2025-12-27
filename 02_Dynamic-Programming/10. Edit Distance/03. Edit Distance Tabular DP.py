# https://leetcode.com/problems/edit-distance/

from typing import List

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n, m = len(word1), len(word2)
        
        # dp[i][j] = min operations to convert word1[0..i] to word2[0..j]
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        
        # Base cases
        for i in range(n + 1):
            dp[i][0] = i  # delete i characters from word1
        for j in range(m + 1):
            dp[0][j] = j  # insert j characters into word1
        
        # Fill the dp table
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]  # no operation needed
                else:
                    # replace, delete, insert
                    dp[i][j] = 1 + min(
                        dp[i - 1][j - 1],  # replace
                        dp[i - 1][j],      # delete from word1
                        dp[i][j - 1]       # insert into word1
                    )
        
        return dp[n][m]


# ---------------- Example Usage ----------------
sol = Solution()

# Example 1
word1 = "horse"
word2 = "ros"
print(sol.minDistance(word1, word2))  # Output: 3

# Example 2
word1 = "intention"
word2 = "execution"
print(sol.minDistance(word1, word2))  # Output: 5

# Example 3
word1 = ""
word2 = "abc"
print(sol.minDistance(word1, word2))  # Output: 3

# Example 4
word1 = "hello"
word2 = "hello"
print(sol.minDistance(word1, word2))  # Output: 0

# Example 5
word1 = "a"
word2 = "b"
print(sol.minDistance(word1, word2))  # Output: 1

# Example 6
word1 = "zoologicoarchaeologist"
word2 = "zoogeologist"
print(sol.minDistance(word1, word2))  # Output: 10