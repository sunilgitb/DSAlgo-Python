# https://leetcode.com/problems/excel-sheet-column-number/

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        p = 1
        ans = 0
        
        for ch in columnTitle[::-1]:
            ans += p * (ord(ch) - 64)
            p *= 26
        
        return ans


# -------- Driver Code --------
solution = Solution()

print(solution.titleToNumber("A"))     # 1
print(solution.titleToNumber("Z"))     # 26
print(solution.titleToNumber("AA"))    # 27
print(solution.titleToNumber("ZY"))    # 701
print(solution.titleToNumber("ABCD"))  # 19010
