"""
File: 04. Grid Unique Paths.py
Problem:
Count number of unique paths from top-left to bottom-right
in an m x n grid. You can only move RIGHT or DOWN.

LeetCode:
https://leetcode.com/problems/unique-paths/
"""

# ------------------------------------------------------------
# Approach 1: Dynamic Programming (2D DP)
# Time Complexity: O(m * n)
# Space Complexity: O(m * n)
# ------------------------------------------------------------

def unique_paths_dp(m: int, n: int) -> int:
    dp = [[0] * n for _ in range(m)]

    # First row and first column have only 1 way
    for i in range(m):
        dp[i][0] = 1
    for j in range(n):
        dp[0][j] = 1

    # Fill DP table
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    return dp[m - 1][n - 1]


# ------------------------------------------------------------
# Approach 2: Space Optimized DP (1D Array)
# Time Complexity: O(m * n)
# Space Complexity: O(n)
# ------------------------------------------------------------

def unique_paths_optimized(m: int, n: int) -> int:
    dp = [1] * n

    for _ in range(1, m):
        for j in range(1, n):
            dp[j] = dp[j] + dp[j - 1]

    return dp[n - 1]


# ------------------------------------------------------------
# Approach 3: Mathematical Combination
# Total moves = (m-1) DOWN + (n-1) RIGHT
# Answer = C(m+n-2, m-1)
# Time Complexity: O(min(m, n))
# Space Complexity: O(1)
# ------------------------------------------------------------

def unique_paths_math(m: int, n: int) -> int:
    N = m + n - 2
    r = min(m - 1, n - 1)

    res = 1
    for i in range(1, r + 1):
        res = res * (N - r + i) // i

    return res


# ------------------------------------------------------------
# Driver Code
# ------------------------------------------------------------
if __name__ == "__main__":
    test_cases = [
        (3, 7),
        (3, 2),
        (7, 3),
        (3, 3),
        (1, 1)
    ]

    print("Using 2D DP:")
    for m, n in test_cases:
        print(f"Grid ({m} x {n}) -> {unique_paths_dp(m, n)}")

    print("\nUsing Space Optimized DP:")
    for m, n in test_cases:
        print(f"Grid ({m} x {n}) -> {unique_paths_optimized(m, n)}")

    print("\nUsing Mathematical Formula:")
    for m, n in test_cases:
        print(f"Grid ({m} x {n}) -> {unique_paths_math(m, n)}")


"""
Output:
Using 2D DP:
Grid (3 x 7) -> 28
Grid (3 x 2) -> 3
Grid (7 x 3) -> 28
Grid (3 x 3) -> 6
Grid (1 x 1) -> 1

Using Space Optimized DP:
Grid (3 x 7) -> 28
Grid (3 x 2) -> 3
Grid (7 x 3) -> 28
Grid (3 x 3) -> 6
Grid (1 x 1) -> 1

Using Mathematical Formula:
Grid (3 x 7) -> 28
Grid (3 x 2) -> 3
Grid (7 x 3) -> 28
Grid (3 x 3) -> 6
Grid (1 x 1) -> 1
"""
