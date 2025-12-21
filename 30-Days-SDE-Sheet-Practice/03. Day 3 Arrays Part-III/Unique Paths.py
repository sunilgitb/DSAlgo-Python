# https://leetcode.com/problems/unique-paths/

cclass Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # DP table initialized with 1s
        dp = [[1] * (n + 1) for _ in range(m + 1)]

        # Fill DP table
        for i in range(2, m + 1):
            for j in range(2, n + 1):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[m][n]


# -------------------- DRIVER CODE --------------------
if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        (3, 7),
        (3, 2),
        (7, 3),
        (1, 10),
        (5, 5)
    ]

    for m, n in test_cases:
        print(f"Unique paths for grid {m} x {n}: {sol.uniquePaths(m, n)}")
