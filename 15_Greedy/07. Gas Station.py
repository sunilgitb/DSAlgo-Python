# https://leetcode.com/problems/gas-station/
# Gas Station
# Problem: There are n gas stations along a circular route.
# gas[i] = amount of gas at station i
# cost[i] = cost of gas to travel to next station i+1
# Find the starting station index from which we can complete the circuit,
# or -1 if impossible.

from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """
        Optimized Greedy Approach (O(n) time, O(1) space):
        - If total gas < total cost → impossible → return -1
        - Track cumulative sum (gas[i] - cost[i])
        - Whenever cumulative sum becomes negative → reset start to next station
        - The last reset point + 1 is the correct starting station (if circuit possible)
        """
        if sum(gas) < sum(cost):
            return -1
        
        total_surplus = 0
        start_index = 0
        
        for i in range(len(gas)):
            total_surplus += gas[i] - cost[i]
            if total_surplus < 0:
                # Cannot start from any station between start_index and i
                start_index = i + 1
                total_surplus = 0
        
        return start_index


# Driver Code with multiple test cases
def run_tests():
    test_cases = [
        # Example 1
        ([1, 2, 3, 4, 5], [3, 4, 5, 1, 2], 3),
        
        # Example 2
        ([2, 3, 4], [3, 4, 3], -1),
        
        # All stations possible
        ([5, 5, 5], [5, 5, 5], 0),
        
        # Single station
        ([1], [1], 0),
        ([1], [2], -1),
        
        # Larger example
        ([4, 5, 2, 6, 5, 3], [6, 4, 3, 5, 7, 2], 2),
        
        # All gas < cost
        ([1, 2], [3, 4], -1),
    ]
    
    print("Testing Gas Station Problem\n" + "="*40)
    
    for idx, (gas, cost, expected) in enumerate(test_cases, 1):
        sol = Solution()
        result = sol.canCompleteCircuit(gas, cost)
        status = "✓ PASS" if result == expected else "✗ FAIL"
        print(f"Test {idx:2d}: {status}")
        print(f"   Gas:  {gas}")
        print(f"   Cost: {cost}")
        print(f"   Start Index: {result} (Expected: {expected})")
        print("-" * 40)


if __name__ == "__main__":
    run_tests()``