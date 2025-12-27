class Solution:
    def numTrees(self, n: int) -> int:
        """
        dp[i] = number of unique BSTs that can be formed using i nodes
        """

        dp = [0] * (n + 1)
        dp[0] = 1  # Empty tree

        for i in range(1, n + 1):
            for j in range(i):
                dp[i] += dp[j] * dp[i - j - 1]

        return dp[n]


# ---------------- Example Usage ----------------
if __name__ == "__main__":
    sol = Solution()

    print(sol.numTrees(1))  # Output: 1
    print(sol.numTrees(2))  # Output: 2
    print(sol.numTrees(3))  # Output: 5
    print(sol.numTrees(4))  # Output: 14
