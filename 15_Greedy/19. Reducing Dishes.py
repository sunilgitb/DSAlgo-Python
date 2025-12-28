# https://leetcode.com/problems/reducing-dishes/
# Reducing Dishes
# Problem: Given satisfaction values of dishes, find the maximum satisfaction
#          you can get by cooking some dishes in some order.
#          Cooking time starts from 1, satisfaction = time * satisfaction value.

from typing import List


class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        """
        Optimal Greedy Approach (O(n log n)):
        - Sort satisfaction in ascending order
        - Start adding dishes from the highest (most positive) satisfaction
        - Keep adding as long as the new dish increases the total satisfaction
        - Since later dishes are cooked at higher time, adding positive or small negative
          that compensates previous positives is beneficial
        
        Time Complexity: O(n log n) due to sorting
        Space Complexity: O(1) or O(n) depending on sorting implementation
        """
        # Sort in ascending order
        satisfaction.sort()
        
        total = 0
        result = 0
        
        # Start from the end (largest values)
        while satisfaction and satisfaction[-1] + total > 0:
            total += satisfaction.pop()
            result += total
        
        return result


# Driver Code with comprehensive test cases
def run_tests():
    test_cases = [
        # Example 1
        ([-1, -8, 0, 5, -9], 14),
        
        # Example 2
        ([4, 3, 2], 20),
        
        # Example 3
        ([-1, -4, -5], 0),
        
        # All negative
        ([-10, -9, -8], 0),
        
        # Mixed with zero
        ([-1, 0, 1, 2], 4),
        
        # Single positive
        ([5], 5),
        
        # Empty list
        ([], 0),
    ]
    
    print("Testing Reducing Dishes\n" + "="*40)
    
    for idx, (satisfaction, expected) in enumerate(test_cases, 1):
        sol = Solution()
        result = sol.maxSatisfaction(satisfaction[:])  # copy list
        status = "✓ PASS" if result == expected else "✗ FAIL"
        print(f"Test {idx:2d}: {status}")
        print(f"   Satisfaction: {satisfaction}")
        print(f"   Max satisfaction: {result} (Expected: {expected})")
        print("-" * 40)


if __name__ == "__main__":
    run_tests()