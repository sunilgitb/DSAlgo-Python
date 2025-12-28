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
def run_tests():
    test_cases = [
        # Example 1
        (["flower","flow","flight"], "fl"),
        
        # Example 2
        (["dog","racecar","car"], ""),
        
        # All identical
        (["abc","abc","abc"], "abc"),
        
        # Single string
        (["a"], "a"),
        
        # Empty strings
        (["","abc"], ""),
        
        # One empty string
        (["", ""], ""),
        
        # Longer common prefix
        (["interspecies","interstellar","interstate"], "inters"),
        
        # Different lengths
        (["prefix","pre","pretest"], "pre"),
    ]
    
    print("Testing Longest Common Prefix\n" + "="*50)
    
    sol = Solution()
    
    for idx, (strs, expected) in enumerate(test_cases, 1):
        result = sol.longestCommonPrefix(strs[:])
        status = "✓ PASS" if result == expected else "✗ FAIL"
        print(f"Test {idx:2d}: {status}")
        print(f"   Input:  {strs}")
        print(f"   Output: '{result}'")
        print(f"   Expected: '{expected}'")
        print("-" * 50)


if __name__ == "__main__":
    run_tests()