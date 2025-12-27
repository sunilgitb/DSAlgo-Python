# https://leetcode.com/problems/edit-distance/

from typing import List
from functools import lru_cache

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n, m = len(word1), len(word2)
        
        @lru_cache(None)
        def solve(i: int, j: int) -> int:
            # Base cases: if one string is exhausted
            if i == 0:
                return j  # insert remaining j characters
            if j == 0:
                return i  # delete remaining i characters
            
            # If characters match, no operation needed
            if word1[i - 1] == word2[j - 1]:
                return solve(i - 1, j - 1)
            
            # Try all three operations: replace, delete, insert
            replace = solve(i - 1, j - 1)
            delete  = solve(i - 1, j)
            insert  = solve(i, j - 1)
            
            return 1 + min(replace, delete, insert)
        
        return solve(n, m)


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
word1 = "zoologicoarchaeologist"
word2 = "zoogeologist"
print(sol.minDistance(word1, word2))  # Output: 10

# Example 4 (empty strings)
word1 = ""
word2 = "abc"
print(sol.minDistance(word1, word2))  # Output: 3

# Example 5 (identical strings)
word1 = "hello"
word2 = "hello"
print(sol.minDistance(word1, word2))  # Output: 0

# Example 6
word1 = "a"
word2 = "b"
print(sol.minDistance(word1, word2))  # Output: 1