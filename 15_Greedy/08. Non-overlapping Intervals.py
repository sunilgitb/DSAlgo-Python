# https://leetcode.com/problems/non-overlapping-intervals/
# Non-overlapping Intervals
# Problem: Given an array of intervals, find the minimum number of intervals
#          you need to remove to make the rest non-overlapping.

from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
        Greedy Approach (Optimal):
        - Sort intervals by start time
        - Track the end time of the last non-overlapping interval
        - If current interval overlaps with the previous → remove it
          (greedily keep the one that ends earlier to allow more room for future intervals)
        - Count how many intervals we remove
        
        Time Complexity: O(n log n) due to sorting
        Space Complexity: O(1)
        """
        if not intervals:
            return 0
        
        # Sort by start time (and by end time if start times are equal)
        intervals.sort(key=lambda x: x[0])
        
        count = 0
        prev_end = intervals[0][1]
        
        for i in range(1, len(intervals)):
            curr_start, curr_end = intervals[i]
            
            # Overlap detected
            if curr_start < prev_end:
                # Remove current interval (greedily prefer the one ending earlier)
                count += 1
                prev_end = min(prev_end, curr_end)
            else:
                # No overlap → keep current interval
                prev_end = curr_end
        
        return count


# Driver Code with multiple test cases
def run_tests():
    test_cases = [
        # Example 1
        ([[1,2],[2,3],[3,4],[1,3]], 1),    # Remove [1,3]
        
        # Example 2
        ([[1,2],[1,2],[1,2]], 2),         # Remove two [1,2]
        
        # Example 3
        ([[1,2],[2,3]], 0),               # No overlap
        
        # All overlapping
        ([[1,100],[1,100],[1,100]], 2),
        
        # Single interval
        ([[5,10]], 0),
        
        # Empty list
        ([], 0),
        
        # Complex case
        ([[1,3],[2,4],[3,6],[5,7],[6,8]], 2),
    ]
    
    print("Testing Non-overlapping Intervals\n" + "="*50)
    
    for idx, (intervals, expected) in enumerate(test_cases, 1):
        sol = Solution()
        result = sol.eraseOverlapIntervals(intervals)
        status = "✓ PASS" if result == expected else "✗ FAIL"
        print(f"Test {idx:2d}: {status}")
        print(f"   Intervals: {intervals}")
        print(f"   Intervals to remove: {result} (Expected: {expected})")
        print("-" * 50)


if __name__ == "__main__":
    run_tests()