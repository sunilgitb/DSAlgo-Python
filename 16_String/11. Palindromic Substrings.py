# https://leetcode.com/problems/palindromic-substrings/

class Solution:
    def countSubstrings(self, s: str) -> int:
        def getPalCounts(l, r):
            count = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
            return count
        
        res = 0
        for i in range(len(s)):
            res += getPalCounts(i, i)    # odd length palindromes
            res += getPalCounts(i, i+1)  # even length palindromes
        
        return res


# -------- Driver Code --------
solution = Solution()

print(solution.countSubstrings("abc"))   # 3
print(solution.countSubstrings("aaa"))   # 6
print(solution.countSubstrings("aba"))   # 4
print(solution.countSubstrings("abba"))  # 6
print(solution.countSubstrings(""))      # 0
