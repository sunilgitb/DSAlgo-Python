from collections import defaultdict

class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        """
        Find the number of unique non-empty substrings of p that are also substrings 
        of the infinite wraparound string "...zabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcd..."
        
        Key Insight:
        - The wraparound string is essentially the alphabet in cyclic order
        - A substring is valid if it's a contiguous sequence in the cyclic alphabet
        - Example: "abc", "zab", "xyzab" are valid; "acb", "az" are not
        
        Approach:
        - Track the longest contiguous sequence ending at each character
        - The count of unique substrings ending with character c is equal to 
          the length of the longest valid sequence ending with c
        - Sum these counts for all characters 'a' to 'z'
        """
        
        if not p:
            return 0
        
        # Dictionary to store the longest valid substring ending with each character
        dp = defaultdict(int)
        streak = 0
        
        for i in range(len(p)):
            # Check if current character follows previous in cyclic alphabet
            if i > 0 and (ord(p[i]) - ord(p[i-1]) == 1 or (p[i-1] == 'z' and p[i] == 'a')):
                streak += 1
            else:
                streak = 1
            
            # Update the maximum streak ending with current character
            dp[p[i]] = max(dp[p[i]], streak)
        
        # Sum of all maximum streaks gives total unique substrings
        return sum(dp.values())


# Alternative implementation (more concise)
class Solution2:
    def findSubstringInWraproundString(self, p: str) -> int:
        p, dp, streak = '0' + p, defaultdict(int), 0
        
        for i in range(1, len(p)):
            # Check if consecutive characters are in cyclic order
            if (ord(p[i-1]) - 96) % 26 == (ord(p[i]) - 97):
                streak += 1
            else:
                streak = 1
            dp[p[i]] = max(dp[p[i]], streak)
        
        return sum(dp.values())


# Alternative implementation using string checking
class Solution3:
    def findSubstringInWraproundString(self, p: str) -> int:
        from collections import defaultdict
        
        p = '0' + p  # Add dummy character to simplify boundary check
        dp = defaultdict(int)
        lo = 0  # Start index of current valid streak
        
        for hi in range(1, len(p)):
            # Check if two consecutive characters are in cyclic alphabetical order
            if p[hi-1] + p[hi] not in 'abcdefghijklmnopqrstuvwxyza':
                lo = hi
            dp[p[hi]] = max(dp[p[hi]], hi + 1 - lo)
        
        return sum(dp.values())


# Driver code with test cases
if __name__ == "__main__":
    solution = Solution()
    solution2 = Solution2()
    solution3 = Solution3()
    
    test_cases = [
        "a",          # Expected: 1 ("a")
        "cac",        # Expected: 2 ("c", "a")
        "zab",        # Expected: 6 ("z", "a", "b", "za", "ab", "zab")
        "abc",        # Expected: 6 ("a", "b", "c", "ab", "bc", "abc")
        "abcd",       # Expected: 10 (all substrings of length 1-4)
        "zabx",       # Expected: 7 ("z", "a", "b", "x", "za", "ab", "zab")
        "",           # Expected: 0
        "aaaa",       # Expected: 4 ("a" at positions 0,1,2,3 but all same substring)
        "abcdefghijklmnopqrstuvwxyz",  # Expected: 351
        "zabcdefghijklmnopqrstuvwxy",  # Expected: 351 (wraparound)
    ]
    
    expected_results = [1, 2, 6, 6, 10, 7, 0, 4, 351, 351]
    
    print("Testing Unique Substrings in Wraparound String")
    print("=" * 60)
    
    for i, (test, expected) in enumerate(zip(test_cases, expected_results), 1):
        print(f"\nTest Case {i}: p = '{test}'")
        print("-" * 40)
        
        result1 = solution.findSubstringInWraproundString(test)
        result2 = solution2.findSubstringInWraproundString(test)
        result3 = solution3.findSubstringInWraproundString(test)
        
        print(f"Solution 1 result: {result1}")
        print(f"Solution 2 result: {result2}")
        print(f"Solution 3 result: {result3}")
        print(f"Expected result:  {expected}")
        
        if result1 == expected and result1 == result2 == result3:
            print("✓ All solutions match expected result")
        else:
            print("✗ Results differ")
    
    # Additional explanation
    print("\n" + "=" * 60)
    print("EXPLANATION:")
    print("=" * 60)
    print("\nFor p = 'zab':")
    print("- Valid substrings are all substrings that appear in wraparound alphabet")
    print("- Wraparound alphabet: ...xyzabcdefghijklmnopqrstuvwxyzabc...")
    print("- 'zab' appears in: ...wxyzabc...")
    print("- All substrings: 'z', 'a', 'b', 'za', 'ab', 'zab' = 6 unique substrings")
