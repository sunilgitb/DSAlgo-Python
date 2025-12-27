# https://leetcode.com/problems/burst-balloons/
# https://youtu.be/uG_MtaCJIrM

from typing import List

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # Add sentinel balloons with value 1 on both ends
        nums = [1] + nums + [1]
        n = len(nums)
        
        # dp[l][r] = max coins obtained by bursting balloons from index l to r (inclusive)
        dp = [[-1] * n for _ in range(n)]
        
        def solve(l: int, r: int) -> int:
            if l > r:
                return 0
            if dp[l][r] != -1:
                return dp[l][r]
            
            max_coins = 0
            # Try bursting every possible balloon k as the last one in [l, r]
            for k in range(l, r + 1):
                coins = nums[l - 1] * nums[k] * nums[r + 1]  # coins from bursting k last
                coins += solve(l, k - 1) + solve(k + 1, r)    # coins from left & right subproblems
                max_coins = max(max_coins, coins)
            
            dp[l][r] = max_coins
            return max_coins
        
        # Solve for bursting balloons from index 1 to n-2 (excluding sentinels)
        return solve(1, n - 2)


# ---------------- Example Usage ----------------
sol = Solution()

# Example 1 (LeetCode)
nums = [3, 1, 5, 8]
print(sol.maxCoins(nums))  # Output: 167

# Example 2
nums = [1, 5]
print(sol.maxCoins(nums))  # Output: 10

# Example 3
nums = [1]
print(sol.maxCoins(nums))  # Output: 1

# Example 4
nums = [9, 1, 8, 3, 2]
print(sol.maxCoins(nums))  # Output: 342

# Example 5
nums = [1, 2, 3, 4, 5]
print(sol.maxCoins(nums))  # Output: 110

# Example 6 (all 1s)
nums = [1, 1, 1, 1]
print(sol.maxCoins(nums))  # Output: 6