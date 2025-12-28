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


# Driver Code
if __name__ == "__main__":
    solution = Solution()
    
    # Test cases
    test_cases = [
        # Example 1
        ([1, 1, 1], 5, 6),
        
        # Example 2
        ([1, 2, 3], 9, 6),
        
        # All 1s
        ([1, 1, 1, 1], 3, 10),
        
        # Larger numbers
        ([2, 3, 4], 10, 5),
        
        # Single element
        ([5], 10, 1),
        ([5], 4, 0),
        
        # All subarrays invalid
        ([10, 20, 30], 5, 0),
        
        # Empty array
        ([], 10, 0),
    ]
    
    print("Testing Count Subarrays With Score Less Than K\n" + "="*60)
    
    for idx, (nums, k, expected) in enumerate(test_cases, 1):
        result = solution.countSubarrays(nums, k)
        status = "✓ PASS" if result == expected else "✗ FAIL"
        print(f"Test {idx:2d}: {status}")
        print(f"   nums: {nums}")
        print(f"   k:    {k}")
        print(f"   Output: {result} (Expected: {expected})")
        print("-" * 60)