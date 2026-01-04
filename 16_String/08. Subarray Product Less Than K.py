# https://leetcode.com/problems/subarray-product-less-than-k/
# Subarray Product Less Than K
# Problem: Given an array of positive integers nums and an integer k,
# return the number of contiguous subarrays where the product of all elements is strictly less than k.

from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        """
        Sliding Window (Two Pointers) - Optimal O(n) time, O(1) space
        
        Maintain a window [left, right] where product < k.
        For each right, add (right - left + 1) valid subarrays ending at right.
        Shrink from left when product >= k.
        """
        if k <= 1:
            return 0  # No subarray can have product < k (since nums > 0)
        
        left = 0
        product = 1
        count = 0
        
        for right in range(len(nums)):
            product *= nums[right]
            
            # Shrink window until product < k
            while product >= k and left <= right:
                product //= nums[left]
                left += 1
            
            # All subarrays ending at right are valid
            count += right - left + 1
        
        return count


# Driver Code with # Driver Code (simple & clean like longestCommonPrefix example)

solution = Solution()

nums = [10, 5, 2, 6]
k = 100
print(solution.numSubarrayProductLessThanK(nums, k))  # 8

nums = [1, 2, 3]
k = 0
print(solution.numSubarrayProductLessThanK(nums, k))  # 0

nums = [1, 1, 1, 1]
k = 2
print(solution.numSubarrayProductLessThanK(nums, k))  # 10

nums = [5]
k = 6
print(solution.numSubarrayProductLessThanK(nums, k))  # 1

nums = [5]
k = 4
print(solution.numSubarrayProductLessThanK(nums, k))  # 0

nums = [2, 3, 4, 5]
k = 20
print(solution.numSubarrayProductLessThanK(nums, k))  # 7

nums = [10, 20, 30]
k = 5
print(solution.numSubarrayProductLessThanK(nums, k))  # 0
