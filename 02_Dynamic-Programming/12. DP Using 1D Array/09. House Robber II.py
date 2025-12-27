class Solution:
    def rob(self, nums):
        # In circular houses, first and last are neighbors
        if len(nums) == 1:
            return nums[0]

        def houseRobber1(arr):
            n = len(arr)
            if n == 0:
                return 0
            if n == 1:
                return arr[0]

            dp = [0] * (n + 1)
            dp[0] = 0
            dp[1] = arr[0]

            for i in range(2, n + 1):
                dp[i] = max(dp[i - 1], dp[i - 2] + arr[i - 1])

            return dp[n]

        # Case 1: Exclude first house
        res1 = houseRobber1(nums[1:])

        # Case 2: Exclude last house
        res2 = houseRobber1(nums[:-1])

        return max(res1, res2)


# ---------------- Example Usage ----------------
if __name__ == "__main__":
    sol = Solution()

    print(sol.rob([2, 3, 2]))
    # Output: 3

    print(sol.rob([1, 2, 3, 1]))
    # Output: 4

    print(sol.rob([1, 2, 3]))
    # Output: 3

    print(sol.rob([5]))
    # Output: 5
