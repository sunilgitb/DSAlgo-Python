# https://leetcode.com/problems/break-a-palindrome/

class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        n = len(palindrome)

        # Single character palindrome cannot be broken
        if n == 1:
            return ''

        # Try replacing the first non-'a' character in the first half
        for i in range(n // 2):
            if palindrome[i] != 'a':
                return palindrome[:i] + 'a' + palindrome[i + 1:]

        # All characters in first half are 'a'
        # Replace last character with 'b'
        return palindrome[:-1] + 'b'


# -------- Driver Code --------
solution = Solution()

print(solution.breakPalindrome("abccba"))  # aaccba
print(solution.breakPalindrome("a"))       # ""
print(solution.breakPalindrome("aa"))      # ab
print(solution.breakPalindrome("aba"))     # abb
print(solution.breakPalindrome("aaa"))     # aab
