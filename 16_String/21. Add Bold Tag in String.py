# https://www.lintcode.com/problem/1127/
# https://leetcode.com/problems/add-bold-tag-in-string/

# https://www.lintcode.com/problem/1127/
# https://leetcode.com/problems/add-bold-tag-in-string/

from typing import List

class Solution:
    def add_bold_tag(self, s: str, dict: List[str]) -> str:
        paint = [False] * len(s)
        
        for i in range(len(s)):
            for w in dict:
                if i + len(w) <= len(s) and s[i:i + len(w)] == w:
                    paint[i:i + len(w)] = [True] * len(w)
        
        res = ""
        for i in range(len(s)):
            if paint[i] and (i == 0 or not paint[i - 1]):
                res += "<b>"
            
            res += s[i]
            
            if paint[i] and (i == len(s) - 1 or not paint[i + 1]):
                res += "</b>"
        
        return res


# -------- Driver Code --------
solution = Solution()

print(solution.add_bold_tag("abcxyz123", ["abc", "123"]))  
# <b>abc</b>xyz<b>123</b>

print(solution.add_bold_tag("aaabbcc", ["aaa", "aab", "bc"]))  
# <b>aaabbc</b>c

print(solution.add_bold_tag("abab", ["ab"]))  
# <b>abab</b>

print(solution.add_bold_tag("hello", ["xyz"]))  
# hello
