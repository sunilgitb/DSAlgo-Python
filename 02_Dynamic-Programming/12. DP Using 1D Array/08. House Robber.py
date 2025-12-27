class Solution:
    def rob(self, nums):
        # Edge cases
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        # DP array
        n = len(nums)
        dp = [0] * (n + 1)

        dp[0] = 0
        dp[1] = nums[0]

        for i in range(2, n + 1):
            dp[i] = max(dp[i - 1], nums[i - 1] + dp[i - 2])

        return dp[n]


# ---------------- Example Usage ----------------
if __name__ == "__main__":
    sol = Solution()

    print(sol.rob([1, 2, 3, 1]))
    # Output: 4

    print(sol.rob([2, 7, 9, 3, 1]))
    # Output: 12

    print(sol.rob([5]))
    # Output: 5

    print(sol.rob([]))
    # Output: 0
