# https://leetcode.com/problems/find-valid-matrix-given-row-and-column-sums/
# Restore Matrix Given Row and Column Sums
# Problem: Given rowSum and colSum arrays, reconstruct a non-negative integer matrix
#          such that the i-th row sums to rowSum[i] and j-th column sums to colSum[j].

from typing import List

class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        """
        Greedy approach:
        - For each cell [i][j], greedily assign the maximum possible value
          that doesn't exceed the remaining rowSum[i] and colSum[j].
        - This works because we can always assign min(rowSum[i], colSum[j])
          to res[i][j] and subtract it from both sums.
        
        Time Complexity: O(m * n)
        Space Complexity: O(m * n)
        """
        m, n = len(rowSum), len(colSum)
        res = [[0] * n for _ in range(m)]
        
        # Make copies so we don't modify input
        row_remain = rowSum[:]
        col_remain = colSum[:]
        
        for i in range(m):
            for j in range(n):
                # Greedily take as much as possible without exceeding either sum
                val = min(row_remain[i], col_remain[j])
                res[i][j] = val
                row_remain[i] -= val
                col_remain[j] -= val
        
        return res


# Driver Code with test cases
def run_tests():
    test_cases = [
        # Example 1
        ([3, 8], [4, 7, 0], [[3,0,0], [1,7,0]]),
        
        # Example 2
        ([1, 0], [1, 0], [[1,0], [0,0]]),
        
        # Example 3
        ([0], [0], [[0]]),
        
        # Larger example
        ([5, 10, 5], [7, 5, 8], [[5,0,0], [2,5,3], [0,0,5]]),
        
        # All zeros
        ([0, 0, 0], [0, 0, 0], [[0,0,0], [0,0,0], [0,0,0]]),
    ]
    
    print("Testing Restore Matrix Given Row and Column Sums\n" + "="*60)
    
    for idx, (rowSum, colSum, expected) in enumerate(test_cases, 1):
        sol = Solution()
        result = sol.restoreMatrix(rowSum[:], colSum[:])
        status = "✓ PASS" if result == expected else "✗ FAIL"
        print(f"Test {idx:2d}: {status}")
        print(f"   rowSum: {rowSum}")
        print(f"   colSum: {colSum}")
        print("   Result:")
        for row in result:
            print(f"      {row}")
        print(f" Expected:")
        for row in expected:
            print(f"      {row}")
        print("-" * 60)


if __name__ == "__main__":
    run_tests()