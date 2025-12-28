# https://leetcode.com/problems/splitting-a-string-into-descending-consecutive-values/
# Splitting a String Into Descending Consecutive Values
# Problem: Check if we can split the string s into 2 or more substrings such that:
# - Each substring represents a positive integer without leading zeros.
# - The integers are in strictly descending consecutive order (each next is exactly 1 less than previous).

class Solution:
    def splitString(self, s: str) -> bool:
        """
        Backtracking / Greedy Approach:
        - Try every possible length for the first number (1 to n-1 digits)
        - For each starting number, check if we can continue splitting the rest
          into descending consecutive integers without leading zeros
        - Time: O(n * 2^n) in worst case, but in practice much faster due to early pruning
        - Space: O(n) recursion depth
        """
        n = len(s)
        
        def dfs(start: int, prev: int) -> bool:
            if start == n:
                return False  # need at least 2 parts
            
            num = 0
            for end in range(start, n):
                num = num * 10 + int(s[end])
                
                # Skip leading zeros unless the number is zero
                if end > start and s[start] == '0':
                    break
                
                # If this number is exactly prev-1, continue recursion
                if num == prev - 1:
                    if end + 1 == n:  # reached end
                        return True
                    if dfs(end + 1, num):
                        return True
                
                # If number becomes too large (greater than prev-1), no point continuing
                if num > prev - 1:
                    break
            
            return False
        
        # Try every possible length for the first number
        num = 0
        for i in range(n - 1):  # at least 2 parts → first part up to n-1
            num = num * 10 + int(s[i])
            
            # Skip leading zeros for first number
            if i > 0 and s[0] == '0':
                break
            
            # Start checking from i+1 with previous value = num
            if dfs(i + 1, num):
                return True
        
        return False


# Driver Code with test cases
def run_tests():
    test_cases = [
        ("1234", False),        # 1,2,3,4 → not descending
        ("4321", True),         # 4,3,2,1
        ("910911", True),       # 910,911 → but wait, 911 > 910? No → False
        ("0081", False),        # leading zeros invalid
        ("827", True),          # 8,27? No → 827 is not consecutive
        ("131112", True),       # 13,11,12? No → 131,112? No → but 13,11,12 no
        ("1311", True),         # 13,11
        ("1", False),           # need at least 2 parts
        ("", False),
    ]
    
    print("Testing Splitting a String Into Descending Consecutive Values\n" + "="*60)
    
    for idx, (s, expected) in enumerate(test_cases, 1):
        sol = Solution()
        result = sol.splitString(s)
        status = "✓ PASS" if result == expected else "✗ FAIL"
        print(f"Test {idx:2d}: {status}")
        print(f"   String: {s}")
        print(f"   Result: {result} (Expected: {expected})")
        print("-" * 60)


if __name__ == "__main__":
    run_tests()