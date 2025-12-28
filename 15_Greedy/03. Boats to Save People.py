# https://leetcode.com/problems/boats-to-save-people/
# Boats to Save People
# Problem: Given an array of people's weights and a boat weight limit,
# find the minimum number of boats needed to rescue all people
# (each boat can carry at most 2 people).

from typing import List

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        """
        Returns the minimum number of boats required.
        
        Approach: Greedy + Two Pointers
        - Sort people by weight
        - Try to pair heaviest possible with lightest possible
        - If pair fits → use one boat for two people
        - Else → use one boat for the heaviest person only
        """
        people.sort()  # sort in ascending order
        left = 0
        right = len(people) - 1
        boats = 0
        
        while left <= right:
            # Check if lightest + heaviest can fit in one boat
            if people[left] + people[right] <= limit:
                # Both go in one boat
                boats += 1
                left += 1
                right -= 1
            else:
                # Only heaviest goes in one boat
                boats += 1
                right -= 1
        
        return boats


# Driver Code with test cases
def run_tests():
    test_cases = [
        # Example 1
        ([1, 2], 3, 1),           # One boat for both
        
        # Example 2
        ([3, 2, 2, 1], 3, 3),     # Boats: (1,2), (2), (3)
        
        # Example 3
        ([3, 5, 3, 4], 5, 4),     # Boats: (3,2? no), (3), (4), (5)
        
        # All can pair
        ([1, 2, 3, 4], 5, 2),     # (1,4), (2,3)
        
        # All need separate boats
        ([5, 5, 5, 5], 5, 4),
        
        # Single person
        ([7], 10, 1),
        
        # Empty list
        ([], 10, 0),
        
        # Large input case
        ([1, 2, 3, 4, 5, 6, 7, 8], 10, 5),
    ]
    
    print("Testing Boats to Save People\n" + "="*40)
    
    for idx, (people, limit, expected) in enumerate(test_cases, 1):
        sol = Solution()
        result = sol.numRescueBoats(people[:], limit)  # copy list
        status = "✓ PASS" if result == expected else "✗ FAIL"
        print(f"Test {idx:2d}: {status}")
        print(f"   People: {people}")
        print(f"   Limit: {limit}")
        print(f"   Boats needed: {result} (Expected: {expected})")
        print("-" * 40)


if __name__ == "__main__":
    run_tests()