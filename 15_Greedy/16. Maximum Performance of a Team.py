# https://leetcode.com/problems/maximum-performance-of-a-team/
# Maximum Performance of a Team
# Problem: Given n engineers with speed[i] and efficiency[i],
# select at most k engineers to form a team with maximum performance:
#   performance = (sum of speeds) * (minimum efficiency in team)

import heapq
from typing import List


class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        """
        Greedy + Min-Heap Approach (Optimal):
        - Sort engineers by efficiency in descending order
        - For each engineer (from highest efficiency to lowest):
          - Add their speed to the current team sum
          - Maintain a min-heap of k speeds (remove smallest if > k)
          - Current performance = (total speed) * (current engineer's efficiency)
          - Update global max performance
        - Since efficiency decreases, min efficiency is always the current one
        
        Time Complexity: O(n log n)
        Space Complexity: O(k) for heap
        """
        MOD = 10**9 + 7
        
        # Pair efficiency and speed, sort by efficiency descending
        engineers = sorted(zip(efficiency, speed), reverse=True)
        
        min_heap = []           # min-heap to keep k largest speeds
        total_speed = 0
        max_performance = 0
        
        for eff, spd in engineers:
            # Add current speed to total
            total_speed += spd
            heapq.heappush(min_heap, spd)
            
            # If we have more than k engineers, remove slowest
            if len(min_heap) > k:
                total_speed -= heapq.heappop(min_heap)
            
            # Update max performance (eff is the minimum in current team)
            current_performance = total_speed * eff
            max_performance = max(max_performance, current_performance)
        
        return max_performance % MOD


# Driver Code with test cases
def run_tests():
    test_cases = [
        # Example 1
        (5, [2,10,3,1,5,8], [5,4,3,9,7,2], 3, 60),
        
        # Example 2
        (6, [1,10,3,10,1,10], [1,1,1,1,1,1], 3, 30),
        
        # Example 3
        (6, [1,10,3,10,1,10], [7,5,4,2,1,1], 3, 68),
        
        # Single engineer
        (1, [5], [10], 1, 50),
        
        # All same efficiency
        (4, [1,2,3,4], [5,5,5,5], 2, 35),
    ]
    
    print("Testing Maximum Performance of a Team\n" + "="*50)
    
    for idx, (n, speed, efficiency, k, expected) in enumerate(test_cases, 1):
        sol = Solution()
        result = sol.maxPerformance(n, speed, efficiency, k)
        status = "✓ PASS" if result == expected else "✗ FAIL"
        print(f"Test {idx:2d}: {status}")
        print(f"   Speed:      {speed}")
        print(f"   Efficiency: {efficiency}")
        print(f"   k:          {k}")
        print(f"   Result:     {result} (Expected: {expected})")
        print("-" * 50)


if __name__ == "__main__":
    run_tests()