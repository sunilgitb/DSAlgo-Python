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


# Driver Code with comprehensive test cases
def run_tests():
    test_cases = [
        # Example 1
        ([10, 5, 2, 6], 100, 8),
        
        # Example 2
        ([1, 2, 3], 0, 0),
        
        # All 1s
        ([1, 1, 1, 1], 2, 10),
        
        # Single element
        ([5], 6, 1),
        ([5], 4, 0),
        
        # Zeros (each [0] is valid if k > 0)
        ([0, 0, 0], 1, 3),
        
        # Mixed
        ([2, 3, 4, 5], 20, 7),
        
        # All elements > k
        ([10, 20, 30], 5, 0),
    ]
    
    print("Testing Subarray Product Less Than K\n" + "="*50)
    
    sol = Solution()
    
    for idx, (nums, k, expected) in enumerate(test_cases, 1):
        result = sol.numSubarrayProductLessThanK(nums[:], k)
        status = "✓ PASS" if result == expected else "✗ FAIL"
        print(f"Test {idx:2d}: {status}")
        print(f"   nums: {nums}")
        print(f"   k:    {k}")
        print(f"   Output: {result} (Expected: {expected})")
        print("-" * 50)


if __name__ == "__main__":
    run_tests()