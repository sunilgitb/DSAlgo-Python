# https://leetcode.com/problems/two-city-scheduling/
# Two City Scheduling
# Problem: There are 2N people and N people should go to city A, N to city B.
# costs[i] = [cost to send i-th person to city A, cost to city B]
# Minimize total cost.

from typing import List


class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        """
        Optimal Greedy Approach (O(n log n)):
        - Compute the difference: costB - costA for each person
        - Sort by this difference (ascending)
        - First N people (smallest diff) → send to city A (cheaper relative to B)
        - Last N people (largest diff) → send to city B (much more expensive in A)
        """
        # Step 1: Calculate costB - costA for each person
        diffs = []
        for a, b in costs:
            diffs.append((b - a, a, b))  # (diff, costA, costB)
        
        # Step 2: Sort by diff ascending
        diffs.sort()
        
        # Step 3: First N → city A, last N → city B
        total_cost = 0
        n = len(costs) // 2
        
        for i in range(len(diffs)):
            if i < n:
                total_cost += diffs[i][1]  # cost to A
            else:
                total_cost += diffs[i][2]  # cost to B
        
        return total_cost


# Driver Code with test cases
def run_tests():
    test_cases = [
        # Example 1
        ([[10,20], [30,200], [400,50], [30,20]], 110),
        
        # Example 2
        ([[259,770], [448,54], [926,667], [184,139], [840,118], [577,469]], 1859),
        
        # All cheaper in A
        ([[1,100], [1,100], [1,100], [1,100]], 4),
        
        # All cheaper in B
        ([[100,1], [100,1], [100,1], [100,1]], 4),
        
        # Mixed
        ([[20,10], [10,20], [30,10], [10,30]], 60),
    ]
    
    print("Testing Two City Scheduling (Greedy)\n" + "="*50)
    
    for idx, (costs, expected) in enumerate(test_cases, 1):
        sol = Solution()
        result = sol.twoCitySchedCost(costs)
        status = "✓ PASS" if result == expected else "✗ FAIL"
        print(f"Test {idx:2d}: {status}")
        print(f"   Costs: {costs}")
        print(f"   Total Cost: {result} (Expected: {expected})")
        print("-" * 50)


if __name__ == "__main__":
    run_tests()