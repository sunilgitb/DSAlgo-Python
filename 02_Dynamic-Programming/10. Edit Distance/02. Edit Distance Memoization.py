# https://leetcode.com/problems/edit-distance/

from typing import List
from functools import lru_cache

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n, m = len(word1), len(word2)
        
        @lru_cache(None)
        def dfs(i: int, j: int) -> int:
            # Base cases: if one string is exhausted
            if i == 0:
                return j  # insert remaining j characters
            if j == 0:
                return i  # delete remaining i characters
            
            # If characters match, no cost, recurse diagonally
            if word1[i - 1] == word2[j - 1]:
                return dfs(i - 1, j - 1)
            
            # Otherwise, take minimum of three operations: insert, delete, replace
            insert  = dfs(i, j - 1)
            delete  = dfs(i - 1, j)
            replace = dfs(i - 1, j - 1)
            
            return 1 + min(insert, delete, replace)
        
        return dfs(n, m)


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

# Example 4 (identical strings)
word1 = "hello"
word2 = "hello"
print(sol.minDistance(word1, word2))  # Output: 0

# Example 5
word1 = "a"
word2 = "b"
print(sol.minDistance(word1, word2))  # Output: 1

# Example 6 (long strings)
word1 = "zoologicoarchaeologist"
word2 = "zoogeologist"
print(sol.minDistance(word1, word2))  # Output: 10