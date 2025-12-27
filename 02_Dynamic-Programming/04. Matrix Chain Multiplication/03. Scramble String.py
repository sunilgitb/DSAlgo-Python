# https://www.youtube.com/watch?v=SqA0o-DGmEw&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=40
# https://leetcode.com/problems/scramble-string/

from typing import Dict

class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        mp: Dict[str, bool] = {}  # Memoization map: key = a + "-" + b
        
        def solve(a: str, b: str) -> bool:
            if len(a) != len(b):
                return False
            
            if a == b:
                return True
            
            if len(a) <= 1:
                return False  # len==0 impossible (checked earlier), len==1 checked by equality
            
            # Early exit if not anagrams
            if sorted(a) != sorted(b):
                return False
            
            key = a + "-" + b
            if key in mp:
                return mp[key]
            
            n = len(a)
            flag = False
            
            for i in range(1, n):
                # No swap case
                no_swap = solve(a[:i], b[:i]) and solve(a[i:], b[i:])
                
                # Swap case
                swap = solve(a[:i], b[n-i:]) and solve(a[i:], b[:n-i])
                
                if no_swap or swap:
                    flag = True
                    break
            
            mp[key] = flag
            return flag
        
        return solve(s1, s2)


# ---------------- Example Usage ----------------
sol = Solution()

# Example 1
s1 = "great"
s2 = "rgeat"
print(sol.isScramble(s1, s2))  # Output: True

# Example 2
s1 = "abcde"
s2 = "caebd"
print(sol.isScramble(s1, s2))  # Output: False

# Example 3
s1 = "a"
s2 = "a"
print(sol.isScramble(s1, s2))  # Output: True

# Example 4
s1 = "ab"
s2 = "ba"
print(sol.isScramble(s1, s2))  # Output: True (swap)

# Example 5
s1 = "great"
s2 = "grate"
print(sol.isScramble(s1, s2))  # Output: False (not scramble)

# Example 6 (longer example)
s1 = "abcdefghijklmn"
s2 = "efghijklmndcab"
print(sol.isScramble(s1, s2))  # Output: True or False (depending on scramble)