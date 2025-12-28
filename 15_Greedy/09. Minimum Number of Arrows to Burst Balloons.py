# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/
# Minimum Number of Arrows to Burst Balloons
# Problem: Given an array of balloons (intervals), find the minimum number of arrows
#          needed to burst all balloons (an arrow can burst all balloons it overlaps).

from typing import List

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        """
        Greedy Approach (Optimal):
        - Sort intervals by end point (earliest ending first)
        - Place arrow at the end of the first balloon
        - For each subsequent balloon:
          - If it doesn't overlap with current arrow position → shoot new arrow
          - Else → current arrow already hits it (no new arrow needed)
        - Update arrow position only when shooting a new one
        
        Time Complexity: O(n log n) due to sorting
        Space Complexity: O(1) extra space
        """
        if not points:
            return 0
        
        # Sort by end point (greedy: cover as many as possible with each arrow)
        points.sort(key=lambda x: x[1])
        
        arrows = 1  # At least one arrow for the first balloon
        arrow_pos = points[0][1]  # Place first arrow at the end of first balloon
        
        for start, end in points[1:]:
            # If current balloon starts after previous arrow → new arrow needed
            if start > arrow_pos:
                arrows += 1
                arrow_pos = end  # Shoot new arrow at this balloon's end
            # Else: current arrow already hits this balloon (start <= arrow_pos)
            # No need to update arrow_pos (greedily keep it as left as possible)
        
        return arrows


# Driver Code with multiple test cases
def run_tests():
    test_cases = [
        # Example 1
        ([[10,16],[2,8],[1,6],[7,12]], 2),
        
        # Example 2
        ([[1,2],[3,4],[5,6],[7,8]], 4),
        
        # Example 3
        ([[1,2],[2,3],[3,4],[4,5]], 2),
        
        # All overlap at one point
        ([[1,10],[2,3],[3,4],[4,5]], 1),
        
        # Single balloon
        ([[5,10]], 1),
        
        # Empty list
        ([], 0),
        
        # Complex case
        ([[9,12],[1,10],[4,11],[8,12],[3,9],[6,16],[7,13]], 2),
    ]
    
    print("Testing Minimum Number of Arrows to Burst Balloons\n" + "="*60)
    
    for idx, (points, expected) in enumerate(test_cases, 1):
        sol = Solution()
        result = sol.findMinArrowShots(points)
        status = "✓ PASS" if result == expected else "✗ FAIL"
        print(f"Test {idx:2d}: {status}")
        print(f"   Points: {points}")
        print(f"   Arrows needed: {result} (Expected: {expected})")
        print("-" * 60)


if __name__ == "__main__":
    run_tests()