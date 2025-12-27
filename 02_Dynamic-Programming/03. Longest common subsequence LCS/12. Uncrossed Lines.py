# https://leetcode.com/problems/uncrossed-lines/

from typing import List

class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        # Longest Common Subsequence (LCS) between nums1 and nums2
        m, n = len(nums1), len(nums2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if nums1[i - 1] == nums2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        return dp[m][n]


# ---------------- Example Usage ----------------
sol = Solution()

# Example 1 (LeetCode)
nums1 = [1, 4, 2]
nums2 = [1, 2, 4]
print(sol.maxUncrossedLines(nums1, nums2))  # Output: 2  (lines: 1→1 and 4→4)

# Example 2 (LeetCode)
nums1 = [2, 5, 1, 2, 5]
nums2 = [10, 5, 2, 1, 5, 2]
print(sol.maxUncrossedLines(nums1, nums2))  # Output: 3

# Example 3 (LeetCode)
nums1 = [1, 3, 7, 1, 7, 5]
nums2 = [1, 9, 2, 5, 1]
print(sol.maxUncrossedLines(nums1, nums2))  # Output: 2

# Example 4
nums1 = [1, 2, 3]
nums2 = [3, 2, 1]
print(sol.maxUncrossedLines(nums1, nums2))  # Output: 1

# Example 5 (identical arrays)
nums1 = [1, 2, 3, 4]
nums2 = [1, 2, 3, 4]
print(sol.maxUncrossedLines(nums1, nums2))  # Output: 4

# Example 6 (no common elements)
nums1 = [1, 3, 5]
nums2 = [2, 4, 6]
print(sol.maxUncrossedLines(nums1, nums2))  # Output: 0