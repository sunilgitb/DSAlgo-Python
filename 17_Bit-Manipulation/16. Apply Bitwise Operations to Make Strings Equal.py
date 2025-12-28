# https://leetcode.com/problems/apply-bitwise-operations-to-make-strings-equal/

# https://leetcode.com/problems/apply-bitwise-operations-to-make-strings-equal/

class Solution:
    def makeStringsEqual(self, s: str, target: str) -> bool:
        return s == target or (int(s, 2) > 0 and int(target, 2) > 0)


# -------- Driver Code --------
solution = Solution()

print(solution.makeStringsEqual("1100", "1010"))  # True
print(solution.makeStringsEqual("0000", "0000"))  # True
print(solution.makeStringsEqual("0000", "0010"))  # False
print(solution.makeStringsEqual("101", "101"))    # True
print(solution.makeStringsEqual("100", "010"))    # True

        
        
# Time complexity: O(n)
