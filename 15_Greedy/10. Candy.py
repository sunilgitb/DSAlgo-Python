# https://leetcode.com/problems/candy/
# Candy Problem
# Problem: Children in a line with ratings. Each child must have at least 1 candy.
# Children with higher rating than neighbor must have more candies than neighbor.
# Find minimum total candies required.

from typing import List

class Solution:
    def candy(self, ratings: List[int]) -> int:
        """
        Two-Pass Greedy Algorithm (Optimal):
        1. Left-to-Right pass: Ensure right neighbor with higher rating gets more candies
        2. Right-to-Left pass: Ensure left neighbor with higher rating gets more candies
        3. Each pass updates candies[i] = max(current, 1 + neighbor's candies)
        
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        n = len(ratings)
        if n == 0:
            return 0
        
        candies = [1] * n
        
        # Left to Right: Ensure ratings[i] > ratings[i-1] => candies[i] > candies[i-1]
        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                candies[i] = candies[i-1] + 1
        
        # Right to Left: Ensure ratings[i] > ratings[i+1] => candies[i] > candies[i+1]
        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                candies[i] = max(candies[i], candies[i+1] + 1)
        
        return sum(candies)


# Driver Code with comprehensive test cases
def run_tests():
    test_cases = [
        # Example 1
        ([1,0,2], 5),              # [2,1,2]
        
        # Example 2
        ([1,2,2], 4),              # [1,2,1]
        
        # All increasing
        ([1,2,3,4,5], 9),          # [1,2,3,4,5]
        
        # All decreasing
        ([5,4,3,2,1], 9),          # [5,4,3,2,1]
        
        # Equal ratings
        ([1,1,1,1], 4),            # [1,1,1,1]
        
        # Peak and valley
        ([1,3,2,1], 7),            # [1,3,2,1]
        
        # Multiple peaks
        ([1,2,87,87,87,2,1], 13),  # [1,2,3,1,1,1,1]
        
        # Single child
        ([1], 1),
        
        # Empty array
        ([], 0),
    ]
    
    print("Testing Candy Problem (Two-Pass Greedy)\n" + "="*50)
    
    for idx, (ratings, expected) in enumerate(test_cases, 1):
        sol = Solution()
        result = sol.candy(ratings)
        status = "✓ PASS" if result == expected else "✗ FAIL"
        print(f"Test {idx:2d}: {status}")
        print(f"   Ratings: {ratings}")
        print(f"   Min candies: {result} (Expected: {expected})")
        print("-" * 50)


if __name__ == "__main__":
    run_tests()