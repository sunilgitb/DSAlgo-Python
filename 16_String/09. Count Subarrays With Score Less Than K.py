# https://leetcode.com/problems/count-subarrays-with-score-less-than-k/
# Count Subarrays With Score Less Than K
# Problem: Given an array of positive integers nums and an integer k,
# return the number of contiguous subarrays where score < k.
# Score of subarray = sum(subarray) * length(subarray)

from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        """
        Sliding Window (Two Pointers) - O(n) time, O(1) space
        
        Maintain window [left, right] where score < k.
        For each right, add (right - left + 1) valid subarrays ending at right.
        Shrink from left when score >= k.
        """
        if k <= 0:
            return 0  # No valid subarray possible
        
        left = 0
        current_sum = 0
        count = 0
        
        for right in range(len(nums)):
            current_sum += nums[right]
            length = right - left + 1
            
            # Shrink window while score >= k
            while current_sum * length >= k and left <= right:
                current_sum -= nums[left]
                left += 1
                length -= 1
            
            # All subarrays ending at right are valid
            count += right - left + 1
        
        return count

# Driver Code (simple & clean)

solution = Solution()

nums = [1, 1, 1]
k = 5
print(solution.countSubarrays(nums, k))  # 6

nums = [1, 2, 3]
k = 9
print(solution.countSubarrays(nums, k))  # 6

nums = [1, 1, 1, 1]
k = 3
print(solution.countSubarrays(nums, k))  # 10

nums = [2, 3, 4]
k = 10
print(solution.countSubarrays(nums, k))  # 5

nums = [5]
k = 10
print(solution.countSubarrays(nums, k))  # 1

nums = [5]
k = 4
print(solution.countSubarrays(nums, k))  # 0

nums = [10, 20, 30]
k = 5
print(solution.countSubarrays(nums, k))  # 0

nums = []
k = 10
print(solution.countSubarrays(nums, k))  # 0
