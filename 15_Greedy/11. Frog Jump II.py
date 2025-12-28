# https://leetcode.com/problems/frog-jump-ii/
# Frog Jump II
# Problem: Given stones sorted in strictly increasing order,
# find the minimum possible maximum jump distance required
# for a frog to jump from stone[0] to stone[n-1],
# jumping to every stone at most once.

from typing import List

class Solution:
    def maxJump(self, stones: List[int]) -> int:
        """
        Optimal Greedy Approach:
        - The frog must visit every stone exactly once.
        - To minimize the maximum jump, the optimal strategy is to always jump
          to the stone two steps ahead (skip one stone).
        - This way, the maximum jump needed is the maximum distance between
          stones[i] and stones[i+2] for all valid i.
        - The first jump (stones[0] to stones[1]) must be included.
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if len(stones) == 2:
            return stones[1] - stones[0]
        
        max_jump = stones[1] - stones[0]  # first jump is mandatory
        
        # Check every possible skip (i to i+2)
        for i in range(len(stones) - 2):
            max_jump = max(max_jump, stones[i + 2] - stones[i])
        
        return max_jump


# Driver Code with comprehensive test cases
def run_tests():
    test_cases = [
        # Example 1
        ([0, 2, 5, 6, 7], 5),      # max jump = 5 (0→5, 5→7 or 0→6, 6→7)
        
        # Example 2
        ([0, 3, 9], 6),            # 0→9 (skip 3) or 0→3→9, max is 6
        
        # Minimal case
        ([0, 10], 10),
        
        # All stones close
        ([0, 1, 2, 3, 4, 5], 2),
        
        # Large gaps
        ([0, 100, 101, 200, 201, 300], 200),
        
        # Increasing gaps
        ([0, 10, 30, 60, 100], 40),
    ]
    
    print("Testing Frog Jump II\n" + "="*40)
    
    for idx, (stones, expected) in enumerate(test_cases, 1):
        sol = Solution()
        result = sol.maxJump(stones)
        status = "✓ PASS" if result == expected else "✗ FAIL"
        print(f"Test {idx:2d}: {status}")
        print(f"   Stones: {stones}")
        print(f"   Min max jump: {result} (Expected: {expected})")
        print("-" * 40)


if __name__ == "__main__":
    run_tests()