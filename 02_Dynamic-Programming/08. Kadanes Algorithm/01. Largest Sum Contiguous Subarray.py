# https://leetcode.com/problems/maximum-subarray/

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Kadane's Algorithm (optimized)
        current_sum = max_sum = nums[0]  # Initialize with first element
        
        for i in range(1, len(nums)):
            # Either extend previous subarray or start new from current element
            current_sum = max(current_sum + nums[i], nums[i])
            # Update maximum sum found so far
            max_sum = max(max_sum, current_sum)
        
        return max_sum


# ---------------- Example Usage ----------------
sol = Solution()

# Example 1
nums = [-2,1,-3,4,-1,2,1,-5,4]
print(sol.maxSubArray(nums))  # Output: 6  (subarray [4,-1,2,1])

# Example 2
nums = [1]
print(sol.maxSubArray(nums))  # Output: 1

# Example 3
nums = [5,4,-1,7,8]
print(sol.maxSubArray(nums))  # Output: 23  (entire array)

# Example 4 (all negative)
nums = [-1,-2,-3,-4]
print(sol.maxSubArray(nums))  # Output: -1  (single element)

# Example 5
nums = [-2,1]
print(sol.maxSubArray(nums))  # Output: 1

# Example 6
nums = [1, -2, 3, -4, 5, -6, 7]
print(sol.maxSubArray(nums))  # Output: 7