# https://www.youtube.com/watch?v=gr2NtY-2QUY&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=44
# https://leetcode.com/problems/super-egg-drop/
# https://practice.geeksforgeeks.org/problems/egg-dropping-puzzle-1587115620/1#

import sys
from typing import Dict, Tuple

class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        # k = eggs, n = floors
        memo: Dict[Tuple[int, int], int] = {}
        
        def solve(eggs: int, floors: int) -> int:
            if floors == 0 or floors == 1:
                return floors
            if eggs == 1:
                return floors
            
            key = (eggs, floors)
            if key in memo:
                return memo[key]
            
            min_attempts = sys.maxsize
            for x in range(1, floors + 1):
                # Worst case: egg breaks → eggs-1, floors below (x-1)
                # Egg survives → eggs, floors above (floors - x)
                breaks = solve(eggs - 1, x - 1)
                survives = solve(eggs, floors - x)
                attempts = 1 + max(breaks, survives)
                min_attempts = min(min_attempts, attempts)
            
            memo[key] = min_attempts
            return min_attempts
        
        return solve(k, n)


# ---------------- Example Usage ----------------
sol = Solution()

# Example 1 (LeetCode)
k = 2  # eggs
n = 6  # floors
print(sol.superEggDrop(k, n))  # Output: 3

# Example 2 (LeetCode)
k = 1
n = 2
print(sol.superEggDrop(k, n))  # Output: 2

# Example 3
k = 2
n = 10
print(sol.superEggDrop(k, n))  # Output: 4

# Example 4
k = 3
n = 14
print(sol.superEggDrop(k, n))  # Output: 4

# Example 5 (GeeksforGeeks classic)
k = 2
n = 36
print(sol.superEggDrop(k, n))  # Output: 8

# Example 6 (small case)
k = 2
n = 1
print(sol.superEggDrop(k, n))  # Output: 1