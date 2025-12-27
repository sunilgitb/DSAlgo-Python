# https://leetcode.com/problems/number-of-longest-increasing-subsequence/

from typing import List

class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        n = len(nums)
        # dp[i] = length of longest increasing subsequence ending at nums[i]
        dp = [1] * n
        
        # count[i] = number of LIS of length dp[i] ending at nums[i]
        count = [1] * n
        
        max_len = 1  # track maximum LIS length
        
        for r in range(n):
            for l in range(r):
                if nums[l] < nums[r]:
                    if dp[l] + 1 > dp[r]:
                        dp[r] = dp[l] + 1
                        count[r] = count[l]  # reset count
                    elif dp[l] + 1 == dp[r]:
                        count[r] += count[l]  # add to existing count
            
            max_len = max(max_len, dp[r])
        
        # Sum counts of all positions where LIS length == max_len
        res = 0
        for i in range(n):
            if dp[i] == max_len:
                res += count[i]
        
        return res


# ---------------- Example Usage ----------------
sol = Solution()

# Example 1
nums = [1,3,5,4,7]
print(sol.findNumberOfLIS(nums))  # Output: 2  (two LIS: [1,3,4,7] and [1,3,5,7])

# Example 2
nums = [2,2,2,2,2]
print(sol.findNumberOfLIS(nums))  # Output: 5  (all single elements are LIS of length 1)

# Example 3
nums = [1,2,4,3,5,4,7,2]
print(sol.findNumberOfLIS(nums))  # Output: 3  (three LIS of length 4)

# Example 4
nums = [1,5,4,3,2,6,7,10,8,9]
print(sol.findNumberOfLIS(nums))  # Output: 4  (four LIS of length 6)

# Example 5
nums = [1]
print(sol.findNumberOfLIS(nums))  # Output: 1

# Example 6 (empty array)
nums = []
print(sol.findNumberOfLIS(nums))  # Output: 0