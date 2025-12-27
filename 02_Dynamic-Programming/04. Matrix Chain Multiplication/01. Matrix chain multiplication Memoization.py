# https://www.youtube.com/watch?v=9uUVFNOT3_Y&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=34
# https://practice.geeksforgeeks.org/problems/matrix-chain-multiplication0303/1#

import sys
from typing import List

class Solution:
    def matrixMultiplication(self, N: int, arr: List[int]) -> int:
        # Memoization table (using -1 as uncomputed)
        dp = [[-1] * (N + 1) for _ in range(N + 1)]
        
        def solve(i: int, j: int) -> int:
            # Base case: single matrix → no multiplication needed
            if i >= j:
                return 0
            
            # If already computed, return cached result
            if dp[i][j] != -1:
                return dp[i][j]
            
            min_cost = sys.maxsize
            # Try every possible place to split the chain
            for k in range(i, j):
                cost = (
                    solve(i, k) +                  # left part
                    solve(k + 1, j) +              # right part
                    arr[i - 1] * arr[k] * arr[j]   # cost of multiplying the two results
                )
                min_cost = min(min_cost, cost)
            
            # Cache the result
            dp[i][j] = min_cost
            return min_cost
        
        # Start from first and last matrix (indices 1 to N-1)
        return solve(1, N - 1)


# ---------------- Example Usage ----------------
sol = Solution()

# Example 1
N = 5
arr = [40, 20, 30, 10, 30]  # matrices: 40×20, 20×30, 30×10, 10×30
print(sol.matrixMultiplication(N, arr))  # Output: 26000

# Example 2
N = 4
arr = [10, 30, 5, 60]  # matrices: 10×30, 30×5, 5×60
print(sol.matrixMultiplication(N, arr))  # Output: 4500

# Example 3
N = 6
arr = [1, 2, 3, 4, 3, 2]
print(sol.matrixMultiplication(N, arr))  # Output: 18

# Example 4
N = 3
arr = [10, 20, 30]  # only 2 matrices: 10×20 and 20×30
print(sol.matrixMultiplication(N, arr))  # Output: 6000

# Example 5 (single matrix)
N = 2
arr = [5, 10]  # only one matrix: 5×10 → no multiplication
print(sol.matrixMultiplication(N, arr))  # Output: 0