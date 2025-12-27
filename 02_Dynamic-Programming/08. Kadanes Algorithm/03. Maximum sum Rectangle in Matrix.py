# https://practice.geeksforgeeks.org/problems/maximum-sum-rectangle2948/1
# https://youtu.be/yCQN096CwWM

from typing import List

class Solution:
    def maximumSumRectangle(self, R: int, C: int, M: List[List[int]]) -> int:
        def kadane(arr: List[int]) -> int:
            max_ending_here = max_so_far = arr[0]
            for x in arr[1:]:
                max_ending_here = max(x, max_ending_here + x)
                max_so_far = max(max_so_far, max_ending_here)
            return max_so_far
        
        max_rectangle = float('-inf')
        
        # Fix left and right columns
        for left in range(C):
            temp = [0] * R  # temp[r] = sum of row r from column left to right
            
            for right in range(left, C):
                # Add current column to temp
                for r in range(R):
                    temp[r] += M[r][right]
                
                # Find maximum subarray sum in temp (Kadane on rows)
                max_rectangle = max(max_rectangle, kadane(temp))
        
        return max_rectangle


# ---------------- Example Usage ----------------
sol = Solution()

# Example 1
R, C = 4, 5
M = [
    [1, 2, -1, -4, -20],
    [-8, -3, 4, 2, 1],
    [3, 8, 10, 1, 3],
    [-4, -1, 1, 7, -6]
]
print(sol.maximumSumRectangle(R, C, M))  # Output: 29

# Example 2
R, C = 2, 2
M = [
    [1, 2],
    [3, 4]
]
print(sol.maximumSumRectangle(R, C, M))  # Output: 10 (entire matrix)

# Example 3 (single row)
R, C = 1, 5
M = [[-2, 1, -3, 4, -1]]
print(sol.maximumSumRectangle(R, C, M))  # Output: 4

# Example 4 (all negative)
R, C = 3, 3
M = [
    [-1, -2, -3],
    [-4, -5, -6],
    [-7, -8, -9]
]
print(sol.maximumSumRectangle(R, C, M))  # Output: -1

# Example 5
R, C = 3, 4
M = [
    [0, 1, 2, -1],
    [3, -1, 4, 5],
    [-2, 3, -4, 6]
]
print(sol.maximumSumRectangle(R, C, M))  # Output: 18