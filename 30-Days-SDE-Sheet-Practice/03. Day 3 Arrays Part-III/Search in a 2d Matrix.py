# https://leetcode.com/problems/search-a-2d-matrix/

'''Approach:
First use binary search to find the row in which the target is present.
Then apply binary search to the target row to check whether target present in targetRow or not.
'''
from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Edge case
        if not matrix or not matrix[0]:
            return False

        # Step 1: Binary search to find the target row
        t = 0
        b = len(matrix) - 1

        while t <= b:
            mid = (t + b) // 2
            if target < matrix[mid][0]:
                b = mid - 1
            elif target > matrix[mid][-1]:
                t = mid + 1
            else:
                break
        else:
            return False  # target row not found

        targetRow = mid

        # Step 2: Binary search inside the row
        l = 0
        r = len(matrix[0]) - 1

        while l <= r:
            mid = (l + r) // 2
            if target < matrix[targetRow][mid]:
                r = mid - 1
            elif target > matrix[targetRow][mid]:
                l = mid + 1
            else:
                return True

        return False


# -------------------- DRIVER CODE --------------------
if __name__ == "__main__":
    matrix = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 60]
    ]

    targets = [3, 13, 30, 1, 60]

    sol = Solution()
    for t in targets:
        print(f"Target {t}: {sol.searchMatrix(matrix, t)}")

# Time: O(log(n) + log(m)) = O(log(m*n)) 
# Space: O(1)