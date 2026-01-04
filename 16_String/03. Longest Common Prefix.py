# https://leetcode.com/problems/longest-common-prefix/
# Longest Common Prefix
# Problem: Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        Optimal O(S) time where S is total characters across all strings
        - Use shortest string as reference (no prefix can be longer than it)
        - For each character position, check if ALL strings have same character
        - Stop when mismatch found or end of any string reached
        
        Time Complexity: O(S) where S = sum of lengths of all strings
        Space Complexity: O(1)
        """
        if not strs:
            return ""
        
        # Use first string as reference
        prefix = strs[0]
        
        for i in range(1, len(strs)):
            # While current string doesn't match prefix, shorten prefix
            while not strs[i].startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        
        return prefix


# Alternative: Character-by-character approach (your version, also correct)
class SolutionCharByChar:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        result = ""
        ref = strs[0]
        
        # Check each character position
        for i in range(len(ref)):
            char = ref[i]
            # Check if ALL strings have same character at position i
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

strs = ["interspecies", "interstellar", "interstate"]
print(solution.longestCommonPrefix(strs))  # inters

strs = ["abc", "abc", "abc"]
print(solution.longestCommonPrefix(strs))  # abc

strs = ["a"]
print(solution.longestCommonPrefix(strs))  # a
