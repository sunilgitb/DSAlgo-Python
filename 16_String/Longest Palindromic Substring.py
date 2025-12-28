# https://leetcode.com/problems/longest-palindromic-substring/

class Solution: 
    def longestPalindrome(self, s: str) -> str:
        res = ""
        for i in range(len(s)):
            # odd length palindrome
            l = i
            r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > len(res):
                    res = s[l:r + 1]
                l -= 1
                r += 1
            
            # even length palindrome
            l = i
            r = i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > len(res):
                    res = s[l:r + 1]
                l -= 1
                r += 1
        
        return res


# -------- Driver Code --------
solution = Solution()

print(solution.longestPalindrome("babad"))  # "bab" or "aba"
print(solution.longestPalindrome("cbbd"))   # "bb"
print(solution.longestPalindrome("a"))      # "a"
print(solution.longestPalindrome("ac"))     # "a" or "c"
print(solution.longestPalindrome("forgeeksskeegfor"))  # "geeksskeeg"
