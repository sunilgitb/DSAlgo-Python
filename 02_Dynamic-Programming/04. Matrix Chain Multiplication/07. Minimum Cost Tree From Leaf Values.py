# https://leetcode.com/problems/minimum-cost-tree-from-leaf-values/description/

from typing import List

class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        n = len(arr)
        
        # Precompute maximum value in every subarray arr[i..j]
        # maxArr[i][j] = max(arr[i], arr[i+1], ..., arr[j])
        maxArr = [[0] * n for _ in range(n)]
        for i in range(n):
            maxVal = arr[i]
            for j in range(i, n):
                maxVal = max(maxVal, arr[j])
                maxArr[i][j] = maxVal
        
        # Memoization cache: (i,j) → minimum cost for subtree on arr[i..j]
        memo = {}
        
        def solve(i: int, j: int) -> int:
            if i == j:
                return 0  # single leaf node → no cost
            
            if (i, j) in memo:
                return memo[(i, j)]
            
            min_cost = float('inf')
            for k in range(i, j):
                left_cost = solve(i, k)
                right_cost = solve(k + 1, j)
                # Cost of current non-leaf node = max(left subtree) * max(right subtree)
                root_cost = maxArr[i][k] * maxArr[k + 1][j]
                total = left_cost + right_cost + root_cost
                min_cost = min(min_cost, total)
            
            memo[(i, j)] = min_cost
            return min_cost
        
        return solve(0, n - 1)


# ---------------- Example Usage ----------------
sol = Solution()

# Example 1 (LeetCode)
arr = [6, 2, 4]
print(sol.mctFromLeafValues(arr))  # Output: 32

# Example 2
arr = [3, 1, 5, 8]
print(sol.mctFromLeafValues(arr))  # Output: 156

# Example 3
arr = [1]
print(sol.mctFromLeafValues(arr))  # Output: 0

# Example 4
arr = [1, 2]
print(sol.mctFromLeafValues(arr))  # Output: 2

# Example 5
arr = [4, 2, 6, 3, 1]
print(sol.mctFromLeafValues(arr))  # Output: 108

# Example 6
arr = [6, 2, 4, 5, 1]
print(sol.mctFromLeafValues(arr))  # Output: 104