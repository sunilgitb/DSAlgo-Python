# https://leetcode.com/problems/longest-common-prefix/
# Longest Common Prefix
# Problem: Find the longest common prefix string amongst an array of strings.

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        Character-by-character comparison (Optimal):
        - Use first string as reference
        - For each character position i, check if ALL strings have same char
        - Stop at first mismatch or end of any string
        
        Time: O(min_len × n) where n = len(strs), min_len = shortest string length
        Space: O(1)
        """
        if not strs:
            return ""
        
        # Edge case: empty string in list
        for s in strs:
            if not s:
                return ""
        
        result = ""
        ref = strs[0]
        
        # Check each character position
        for i in range(len(ref)):
            char = ref[i]
            # Verify ALL strings have same character at position i
            for s in strs:
                if i >= len(s) or s[i] != char:
                    return result
            result += char
        
        return result


# Driver Code with comprehensive test cases
solution = Solution()

strs = ["flower", "flow", "flight"]
print(solution.longestCommonPrefix(strs))  # fl

strs = ["dog", "racecar", "car"]
print(solution.longestCommonPrefix(strs))  # ""

strs = ["abc", "abc", "abc"]
print(solution.longestCommonPrefix(strs))  # abc

strs = ["a"]
print(solution.longestCommonPrefix(strs))  # a

strs = ["", "abc"]
print(solution.longestCommonPrefix(strs))  # ""

strs = ["interspecies", "interstellar", "interstate"]
print(solution.longestCommonPrefix(strs))  # inters

strs = ["prefix", "pre", "pretest"]
print(solution.longestCommonPrefix(strs))  # pre
