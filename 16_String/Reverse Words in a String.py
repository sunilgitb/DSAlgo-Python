# https://leetcode.com/problems/reverse-words-in-a-string/

class Solution:
    def reverseWords(self, s: str) -> str:
        i = 0
        n = len(s)
        res = ""
        
        while i < n:
            if s[i] == " ":
                i += 1
            else:
                j = i
                while j < n and s[j] != " ":
                    j += 1
                subStr = s[i:j]
                if res == "":
                    res = subStr
                else:
                    res = subStr + " " + res
                i = j
        
        return res


# -------- Driver Code --------
solution = Solution()

print(solution.reverseWords("the sky is blue"))        # "blue is sky the"
print(solution.reverseWords("  hello world  "))       # "world hello"
print(solution.reverseWords("a good   example"))      # "example good a"
print(solution.reverseWords("  Bob    Loves  Alice "))# "Alice Loves Bob"
