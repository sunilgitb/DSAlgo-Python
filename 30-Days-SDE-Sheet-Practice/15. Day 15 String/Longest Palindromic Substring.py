# https://leetcode.com/problems/longest-palindromic-substring/

class Solution: 
    def longestPalindrome(self, s: str) -> str:
        res = ""
        for i in range(len(s)):
            l = i; r = i
            # Odd length palindromes
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > len(res):
                    res = s[l:r+1]
                l -= 1
                r += 1
                
        
            l = i; r = i + 1
            # Even length palindromes
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > len(res):
                    res = s[l:r+1]
                l -= 1
                r += 1
                
        
        return res

# Time: O(n * n)
# Space: O(n)

# Explanation:
# The function longestPalindrome takes a string s as input and finds the longest palindromic substring within it.
# It does this by expanding around each character (and between each pair of characters) to check for palindromes.
# The longest palindrome found during these expansions is stored in the variable res, which is returned at the end. 
# Example usage:
sol = Solution()
print(sol.longestPalindrome("babad"))  # Output: "bab" or "aba"
print(sol.longestPalindrome("cbbd"))   # Output: "bb"
# Output: "bb"