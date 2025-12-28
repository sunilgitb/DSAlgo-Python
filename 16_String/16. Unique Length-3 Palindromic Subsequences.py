# https://leetcode.com/problems/unique-length-3-palindromic-subsequences/

import string

class Solution:
    def countPalindromicSubsequence(self, s):
        res = 0
        for c in string.ascii_lowercase:   # 26 characters
            l = s.find(c)                  # first occurrence
            r = s.rfind(c)                 # last occurrence
            if l != -1 and r > l:
                res += len(set(s[l + 1 : r]))  # unique middle characters
        return res


# -------- Driver Code --------
solution = Solution()

print(solution.countPalindromicSubsequence("aabca"))   # 3
print(solution.countPalindromicSubsequence("adc"))     # 0
print(solution.countPalindromicSubsequence("bbcbaba")) # 4
print(solution.countPalindromicSubsequence("aaa"))     # 1
