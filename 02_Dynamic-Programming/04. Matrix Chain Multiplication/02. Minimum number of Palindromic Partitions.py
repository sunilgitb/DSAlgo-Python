```python
# https://www.youtube.com/watch?v=fOUlNlawdAU&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=36
# https://www.youtube.com/watch?v=9h10fqkI7Nk&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=37
# https://practice.geeksforgeeks.org/problems/palindromic-patitioning4845/1#

import sys
from typing import List

class Solution:
    def palindromicPartition(self, string: str) -> int:
        n = len(string)
        dp = [[-1] * n for _ in range(n)]  # dp[i][j] = min cuts needed for s[i..j]
        
        def solve(i: int, j: int) -> int:
            if i >= j:
                return 0  # single char or empty → no cuts needed
            
            if self.isPalindrome(string, i, j):
                return 0  # already a palindrome → no cuts needed
            
            if dp[i][j] != -1:
                return dp[i][j]
            
            min_cuts = sys.maxsize
            for k in range(i, j):
                # Optimized: use precomputed subproblems
                left = dp[i][k] if dp[i][k] != -1 else solve(i, k)
                right = dp[k + 1][j] if dp[k + 1][j] != -1 else solve(k + 1, j)
                
                temp = 1 + left + right
                min_cuts = min(min_cuts, temp)
            
            dp[i][j] = min_cuts
            return dp[i][j]
        
        return solve(0, n - 1)
    
    def isPalindrome(self, s: str, i: int, j: int) -> bool:
        return s[i:j+1] == s[i:j+1][::-1]


# ---------------- Example Usage ----------------
sol = Solution()

# Example 1
s = "aab"
print(sol.palindromicPartition(s))  # Output: 1  ("aa|b")

# Example 2
s = "abab"
print(sol.palindromicPartition(s))  # Output: 1  ("aba|b" or "a|bab")

# Example 3
s = "nitin"
print(sol.palindromicPartition(s))  # Output: 0  ("nitin" is already palindrome)

# Example 4
s = "abc"
print(sol.palindromicPartition(s))  # Output: 2  ("a|b|c")

# Example 5
s = "aaaba"
print(sol.palindromicPartition(s))  # Output: 1  ("aaa|ba" or "aa|aba")

# Example 6
s = "ababab"
print(sol.palindromicPartition(s))  # Output: 2  ("aba|bab" or "ab|abab")

# Example 7 (longer example)
s = "geeks"
print(sol.palindromicPartition(s))  # Output: 4  (worst case: "g|e|e|k|s")
```