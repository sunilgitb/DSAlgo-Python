# https://leetcode.com/problems/longest-increasing-subsequence/
# https://practice.geeksforgeeks.org/problems/longest-increasing-subsequence-1587115620/1

from typing import List
import bisect

# Method 1: Classic DP (O(n²) time, O(n) space)
class SolutionDP:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        n = len(nums)
        dp = [1] * n  # dp[i] = length of LIS ending at index i
        
        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        return max(dp)


# Method 2: Binary Search + Patience Sorting (O(n log n) time, O(n) space)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        tails = []  # tails[i] = smallest tail of all increasing subsequences with length i+1
        
        for num in nums:
            if not tails or num > tails[-1]:
                tails.append(num)
            else:
                # Find the first element in tails which is >= num
                pos = bisect.bisect_left(tails, num)
                tails[pos] = num
        
        return len(tails)


# Method 3: Binary Search (manual implementation, O(n log n) time, O(n) space)
class SolutionManualBS:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        tails = []
        
        for num in nums:
            if not tails or num > tails[-1]:
                tails.append(num)
            else:
                # Binary search to find leftmost position to replace
                left, right = 0, len(tails) - 1
                while left <= right:
                    mid = (left + right) // 2
                    if tails[mid] < num:
                        left = mid + 1
                    else:
                        right = mid - 1
                tails[left] = num
        
        return len(tails)


# ---------------- Example Usage ----------------
sol = Solution()

# Example 1
nums = [10, 9, 2, 5, 3, 7, 101, 18]
print(sol.lengthOfLIS(nums))  # Output: 4  ("2,3,7,101")

# Example 2
nums = [0, 1, 0, 3, 2, 3]
print(sol.lengthOfLIS(nums))  # Output: 4  ("0,1,2,3")

# Example 3
nums = [7, 7, 7, 7, 7]
print(sol.lengthOfLIS(nums))  # Output: 1

# Example 4
nums = [1]
print(sol.lengthOfLIS(nums))  # Output: 1

# Example 5
nums = [1, 3, 6, 7, 9, 4, 10, 5, 6]
print(sol.lengthOfLIS(nums))  # Output: 6  ("1,3,6,7,9,10")

# Example 6 (empty array)
nums = []
print(sol.lengthOfLIS(nums))  # Output: 0