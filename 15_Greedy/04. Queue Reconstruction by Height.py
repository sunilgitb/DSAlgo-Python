# https://leetcode.com/problems/queue-reconstruction-by-height/
# Queue Reconstruction by Height
# Problem: People are represented by [height, k] where k is the number of people
#          in front who are taller or equal height.
# Goal: Reconstruct the queue in correct order.

from typing import List

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        """
        Greedy approach:
        1. Sort people by decreasing height, then increasing k (people with same height).
        2. Insert each person into the result list at index = k (their position).
        
        Time Complexity: O(n²) due to list.insert() in Python
        Space Complexity: O(n)
        """
        # Step 1: Sort by decreasing height, then increasing k for same height
        people.sort(key=lambda x: (-x[0], x[1]))
        
        # Step 2: Insert each person at their k-th position
        result = []
        for person in people:
            result.insert(person[1], person)  # insert at index k
        
        return result


# Driver Code with test cases
def run_tests():
    test_cases = [
        # Example 1
        ([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]], [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]),
        
        # Example 2
        ([[6,0], [5,0], [4,0], [3,2], [2,2], [1,4]], [[4,0], [5,0], [2,2], [3,2], [1,4], [6,0]]),
        
        # All same height
        ([[2,0], [2,1], [2,2]], [[2,0], [2,1], [2,2]]),
        
        # Single person
        ([[1,0]], [[1,0]]),
        
        # Empty list
        ([], []),
        
        # All unique heights
        ([[8,0], [7,1], [6,2], [5,3], [4,4]], [[8,0], [7,1], [6,2], [5,3], [4,4]]),
    ]
    
    print("Testing Queue Reconstruction by Height\n" + "="*50)
    
    for idx, (people, expected) in enumerate(test_cases, 1):
        sol = Solution()
        result = sol.reconstructQueue(people[:])  # copy input
        status = "✓ PASS" if result == expected else "✗ FAIL"
        print(f"Test {idx:2d}: {status}")
        print(f"   Input:  {people}")
        print(f"   Output: {result}")
        print(f" Expected: {expected}")
        print("-" * 50)


if __name__ == "__main__":
    run_tests()