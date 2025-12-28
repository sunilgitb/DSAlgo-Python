# https://leetcode.com/problems/repeated-string-match/

# Method 1 ---------------------------------------  
class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        # Handle edge cases
        if not b:  # b is empty string
            return 0
        if not a:  # a is empty but b is not (b is non-empty from above check)
            return -1
        
        res = 1
        tmp = a
        # Repeat a until it's at least as long as b
        while len(a) < len(b):
            a += tmp
            res += 1
        
        # Check if b is substring of a
        if self.subStr(a, b):
            return res
        
        # Check if b is substring of a + one more repetition
        if self.subStr(a + tmp, b):
            return res + 1
        
        return -1
    
    def subStr(self, a: str, b: str) -> bool:
        """Check if b is a substring of a"""
        # Quick checks
        if not b:
            return True
        if len(b) > len(a):
            return False
        
        for i in range(len(a) - len(b) + 1):
            if a[i] == b[0] and a[i:i+len(b)] == b:
                return True
        return False

# Method 2 ---------------------------------------  
class Solution2:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        # Handle edge cases
        if not b:
            return 0
        if not a:
            return -1
        
        # Calculate minimum repetitions needed
        n = (len(b) - 1) // len(a) + 1  # Ceiling division
        
        # Check n, n+1, n+2 repetitions
        for i in range(3):
            repeated = a * (n + i)
            if self.subStr(repeated, b):
                return n + i
        return -1
    
    def subStr(self, a: str, b: str) -> bool:
        """Check if b is a substring of a"""
        # Quick checks
        if not b:
            return True
        if len(b) > len(a):
            return False
        
        # Built-in method (faster)
        return b in a


# Alternative using KMP for better performance
class SolutionKMP:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        if not b:
            return 0
        if not a:
            return -1
        
        # Build KMP table for pattern b
        def build_kmp_table(pattern):
            table = [0] * len(pattern)
            j = 0
            for i in range(1, len(pattern)):
                while j > 0 and pattern[i] != pattern[j]:
                    j = table[j-1]
                if pattern[i] == pattern[j]:
                    j += 1
                table[i] = j
            return table
        
        def kmp_search(text, pattern):
            if not pattern:
                return 0
            table = build_kmp_table(pattern)
            j = 0
            for i in range(len(text)):
                while j > 0 and text[i] != pattern[j]:
                    j = table[j-1]
                if text[i] == pattern[j]:
                    j += 1
                if j == len(pattern):
                    return i - j + 1
            return -1
        
        # Determine minimum repetitions needed
        min_reps = (len(b) + len(a) - 1) // len(a)
        
        # Try min_reps, min_reps+1, min_reps+2
        for reps in range(min_reps, min_reps + 3):
            repeated = a * reps
            if kmp_search(repeated, b) != -1:
                return reps
        
        return -1


def run_tests():
    test_cases = [
        ("abcd", "cdabcdab", 3),
        ("a", "aa", 2),
        ("a", "a", 1),
        ("abc", "cabcabca", 4),
        ("abc", "def", -1),
        ("a", "", 0),
        ("", "abc", -1),
        ("", "", 0),
        ("abab", "ba", 2),
        ("abab", "ababab", 3),
        ("aaaaaaaaaaaaaaaaaaaa", "a", 1),
        ("aaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaa", 1),
        ("aaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaa", 2),
        ("abcd", "abcdabcd", 2),
        ("abcd", "abcdabcdabcdabcd", 4),
        ("abcd", "d", 1),
        ("abcd", "da", 2),
    ]
    
    print("Testing Repeated String Match\n" + "="*60)
    
    sol1 = Solution()
    sol2 = Solution2()
    sol_kmp = SolutionKMP()
    
    all_pass = True
    
    for idx, (a, b, expected) in enumerate(test_cases, 1):
        result1 = sol1.repeatedStringMatch(a, b)
        result2 = sol2.repeatedStringMatch(a, b)
        result_kmp = sol_kmp.repeatedStringMatch(a, b)
        
        pass1 = result1 == expected
        pass2 = result2 == expected
        pass_kmp = result_kmp == expected
        
        if not (pass1 and pass2 and pass_kmp):
            all_pass = False
        
        print(f"Test {idx:2d}: {'✓ PASS' if pass1 and pass2 and pass_kmp else '✗ FAIL'}")
        print(f"   a = '{a}'")
        print(f"   b = '{b}'")
        print(f"   Method 1: {result1:2d}, Method 2: {result2:2d}, KMP: {result_kmp:2d} (Expected: {expected:2d})")
        if not (pass1 and pass2 and pass_kmp):
            print(f"   MISMATCH!")
        print("-" * 60)
    
    print(f"\nOverall: {'ALL TESTS PASSED ✓' if all_pass else 'SOME TESTS FAILED ✗'}")
    
    # Additional analysis
    print("\n" + "="*60)
    print("ALGORITHM ANALYSIS")
    print("="*60)
    print("""
    Method 1 (Naive Approach):
    - Time Complexity: O(n * m) in worst case (n = len(a), m = len(b))
    - Space Complexity: O(n + m)
    - Pros: Simple to understand
    - Cons: Inefficient for large strings
    
    Method 2 (Optimized):
    - Time Complexity: O(n * m) in worst case
    - Space Complexity: O(n + m)
    - Pros: Calculates exact range to check
    
    Method 3 (KMP):
    - Time Complexity: O(n + m)
    - Space Complexity: O(m) for KMP table
    - Pros: Linear time, handles worst cases efficiently
    - Cons: More complex implementation
    
    Why we only need to check up to n+2 repetitions:
    - The worst case is when b starts from the end of one a and ends at the 
      beginning of another a
    - Example: a="abc", b="cabcabca" needs 4 repetitions
    - Mathematically, we need at most ceil(len(b)/len(a)) + 1 repetitions
    """)
    
    # Performance test with large strings
    print("\n" + "="*60)
    print("PERFORMANCE TEST SIMULATION")
    print("="*60)
    
    import time
    
    # Create test case with large strings
    large_a = "abcde" * 1000  # 5000 chars
    large_b = "deabc" + "abcde" * 999  # Pattern that needs matching
    
    print(f"Large test case:")
    print(f"  len(a) = {len(large_a)}")
    print(f"  len(b) = {len(large_b)}")
    
    start = time.time()
    result1 = sol1.repeatedStringMatch(large_a, large_b)
    time1 = time.time() - start
    
    start = time.time()
    result2 = sol2.repeatedStringMatch(large_a, large_b)
    time2 = time.time() - start
    
    start = time.time()
    result_kmp = sol_kmp.repeatedStringMatch(large_a, large_b)
    time_kmp = time.time() - start
    
    print(f"\nResults (all should be 2):")
    print(f"  Method 1: {result1}, Time: {time1:.6f}s")
    print(f"  Method 2: {result2}, Time: {time2:.6f}s")
    print(f"  KMP:      {result_kmp}, Time: {time_kmp:.6f}s")


if __name__ == "__main__":
    run_tests()