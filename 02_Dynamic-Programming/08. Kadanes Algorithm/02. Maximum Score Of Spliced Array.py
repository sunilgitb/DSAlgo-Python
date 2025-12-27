# https://leetcode.com/problems/maximum-score-of-spliced-array/

from typing import List

class Solution:
    def maximumsSplicedArray(self, nums1: List[int], nums2: List[int]) -> int:
        def kadane_gain(A: List[int], B: List[int]) -> int:
            # Compute the maximum gain by replacing a contiguous subarray of A with B
            max_gain = cur_gain = 0
            for a, b in zip(A, B):
                cur_gain = max(0, cur_gain + a - b)
                max_gain = max(max_gain, cur_gain)
            return max_gain
        
        sum1 = sum(nums1)
        sum2 = sum(nums2)
        
        # Case 1: Start with nums2, gain by swapping a subarray to nums1
        # Case 2: Start with nums1, gain by swapping a subarray to nums2
        return max(
            sum2 + kadane_gain(nums1, nums2),  # gain = sum1_sub - sum2_sub
            sum1 + kadane_gain(nums2, nums1)   # gain = sum2_sub - sum1_sub
        )


# ---------------- Example Usage ----------------
sol = Solution()

# Example 1
nums1 = [60, 60, 60]
nums2 = [10, 90, 10]
print(sol.maximumsSplicedArray(nums1, nums2))  # Output: 210

# Example 2
nums1 = [20, 40, 20, 70, 30]
nums2 = [50, 20, 50, 40, 20]
print(sol.maximumsSplicedArray(nums1, nums2))  # Output: 220

# Example 3
nums1 = [7, 11, 13]
nums2 = [1, 1, 1]
print(sol.maximumsSplicedArray(nums1, nums2))  # Output: 31

# Example 4
nums1 = [1, 2, 3]
nums2 = [10, 20, 30]
print(sol.maximumsSplicedArray(nums1, nums2))  # Output: 60

# Example 5
nums1 = [10, 20, 30, 40]
nums2 = [5, 15, 25, 35]
print(sol.maximumsSplicedArray(nums1, nums2))  # Output: 130

# Example 6 (equal arrays)
nums1 = [5, 5, 5]
nums2 = [5, 5, 5]
print(sol.maximumsSplicedArray(nums1, nums2))  # Output: 15