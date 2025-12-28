# https://leetcode.com/problems/maximum-units-on-a-truck/
# Maximum Units on a Truck
# Problem: Given boxTypes[i] = [numberOfBoxes_i, unitsPerBox_i] and truckSize,
# select boxes to maximize total units placed on the truck.

from typing import List


class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        """
        Greedy Approach (Optimal):
        - Sort boxes by unitsPerBox in descending order
        - Take as many boxes as possible from the highest unit boxes first
        - If remaining truck space < current box count → take partial
        
        Time Complexity: O(n log n) due to sorting
        Space Complexity: O(1) extra space (excluding input)
        """
        # Sort by unitsPerBox descending
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        
        total_units = 0
        remaining_space = truckSize
        
        for num_boxes, units_per_box in boxTypes:
            # If we can take all boxes of this type
            if num_boxes <= remaining_space:
                total_units += num_boxes * units_per_box
                remaining_space -= num_boxes
            else:
                # Take as many as possible from this type
                total_units += remaining_space * units_per_box
                remaining_space = 0
                break  # truck is full
        
        return total_units


# Driver Code with test cases
def run_tests():
    test_cases = [
        # Example 1
        ([[1, 3], [2, 2], [3, 1]], 4, 8),
        
        # Example 2
        ([[5, 10], [2, 5], [4, 7], [3, 9]], 10, 91),
        
        # Truck too small
        ([[1, 10], [2, 20]], 1, 10),
        
        # All boxes fit
        ([[1, 1], [2, 2], [3, 3]], 6, 1 + 2*2 + 3*3),
        
        # Empty truck
        ([[1, 10]], 0, 0),
        
        # No boxes
        ([], 10, 0),
    ]
    
    print("Testing Maximum Units on a Truck\n" + "="*50)
    
    for idx, (boxTypes, truckSize, expected) in enumerate(test_cases, 1):
        sol = Solution()
        result = sol.maximumUnits(boxTypes[:], truckSize)
        status = "✓ PASS" if result == expected else "✗ FAIL"
        print(f"Test {idx:2d}: {status}")
        print(f"   Box Types: {boxTypes}")
        print(f"   Truck Size: {truckSize}")
        print(f"   Max Units: {result} (Expected: {expected})")
        print("-" * 50)


if __name__ == "__main__":
    run_tests()