# https://leetcode.com/problems/longest-happy-string/
# Longest Happy String
# Problem: Given counts a, b, c for characters 'a', 'b', 'c'.
# Construct the longest string where no three same characters are consecutive.

import heapq
from typing import List


class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        """
        Greedy + Max Heap Approach (Optimal)
        - Use max-heap to always pick the character with highest remaining count
        - If last two characters are the same as the current top → pick second highest
        - Otherwise pick the top one
        """
        # Create max-heap (negative counts for max-heap behavior)
        max_heap = []
        if a > 0:
            heapq.heappush(max_heap, (-a, 'a'))
        if b > 0:
            heapq.heappush(max_heap, (-b, 'b'))
        if c > 0:
            heapq.heappush(max_heap, (-c, 'c'))
        
        result = []
        
        while max_heap:
            # Get the character with highest remaining count
            count1, char1 = heapq.heappop(max_heap)
            
            # If last two characters are same as char1 → use second best
            if len(result) >= 2 and result[-1] == result[-2] == char1:
                if not max_heap:
                    break  # cannot continue
                count2, char2 = heapq.heappop(max_heap)
                result.append(char2)
                if count2 + 1 < 0:  # still some left
                    heapq.heappush(max_heap, (count2 + 1, char2))
                # Push back the first one
                heapq.heappush(max_heap, (count1, char1))
            else:
                # Safe to use char1
                result.append(char1)
                if count1 + 1 < 0:
                    heapq.heappush(max_heap, (count1 + 1, char1))
        
        return ''.join(result)


# Driver Code with test cases
def run_tests():
    test_cases = [
        # Example 1
        (1, 1, 7, "ccaccbcc"),  # or similar
        
        # Example 2
        (7, 1, 0, "aabaa"),
        
        # Example 3
        (1, 2, 3, "ccbcba"),
        
        # All equal
        (5, 5, 5, "ccbbccaabbccaabbccaa"),
        
        # One is zero
        (3, 0, 2, "ccbaa"),
        
        # Single character
        (0, 0, 10, "cc"),
        
        # Impossible to use more than 2
        (0, 0, 3, "cc"),
    ]
    
    print("Testing Longest Happy String\n" + "="*40)
    
    for idx, (a, b, c, expected) in enumerate(test_cases, 1):
        sol = Solution()
        result = sol.longestDiverseString(a, b, c)
        status = "✓ PASS" if len(result) >= len(expected) else "✗ FAIL"
        print(f"Test {idx:2d}: {status}")
        print(f"   a={a}, b={b}, c={c}")
        print(f"   Output: {result}")
        print(f"   Expected length >=: {len(expected)}")
        print("-" * 40)


if __name__ == "__main__":
    run_tests()