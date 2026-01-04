# https://leetcode.com/problems/backspace-string-compare/
# Backspace String Compare
# Problem: Given two strings s and t, return true if they are equal when both are typed into empty text editors.
# '#' means backspace character.

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        """
        Two-pointer approach (O(1) space):
        - Traverse both strings from right to left
        - Skip characters that are backspaced (by counting '#' and skipping previous chars)
        - Compare valid characters from both strings
        """
        i = len(s) - 1
        j = len(t) - 1
        
        while i >= 0 or j >= 0:
            # Find the next valid character in s
            while i >= 0:
                if s[i] == '#':
                    # Skip the backspace and the character it deletes
                    bs = 1
                    i -= 1
                    while i >= 0 and bs > 0:
                        if s[i] == '#':
                            bs += 1
                        else:
                            bs -= 1
                        i -= 1
                else:
                    break
            
            # Find the next valid character in t
            while j >= 0:
                if t[j] == '#':
                    bs = 1
                    j -= 1
                    while j >= 0 and bs > 0:
                        if t[j] == '#':
                            bs += 1
                        else:
                            bs -= 1
                        j -= 1
                else:
                    break
            
            # If one string is exhausted and the other isn't → mismatch
            if (i >= 0) != (j >= 0):
                return False
            
            # If both have valid characters but they differ → mismatch
            if i >= 0 and j >= 0 and s[i] != t[j]:
                return False
            
            # Move to next characters
            i -= 1
            j -= 1
        
        return True


# Driver code with test cases
# ---------------- DRIVER CODE ----------------
solution = Solution()

s = "ab#c"
t = "ad#c"

print(solution.backspaceCompare(s, t))  # True


