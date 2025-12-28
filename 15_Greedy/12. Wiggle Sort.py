# https://leetcode.com/problems/wiggle-sort/
# https://www.lintcode.com/problem/508/
# Wiggle Sort: Rearrange array such that nums[0] < nums[1] > nums[2] < nums[3] > ...

from typing import List


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        O(n log n) time - Sort + Swap every pair
        In-place, modifies nums directly
        """
        nums.sort()  # sort in ascending order
        
        # Swap every pair starting from index 1
        for i in range(1, len(nums) - 1, 2):
            nums[i], nums[i + 1] = nums[i + 1], nums[i]
        
        # No return needed (in-place modification)

    def wiggleSortLinear(self, nums: List[int]) -> None:
        """
        O(n) time - One pass with conditional swaps
        Simpler and faster in practice (no sorting)
        """
        for i in range(1, len(nums)):
            # Even indices (0-based): should be smaller than previous
            if i % 2 == 0 and nums[i] < nums[i - 1]:
                nums[i], nums[i - 1] = nums[i - 1], nums[i]
            
            # Odd indices: should be larger than previous
            elif i % 2 == 1 and nums[i] > nums[i - 1]:
                nums[i], nums[i - 1] = nums[i - 1], nums[i]
        
        # No return needed (in-place)


# Driver Code with test cases
def run_tests():
    test_cases = [
        # Basic examples
        ([1, 5, 1, 1, 6, 4], [1, 4, 1, 5, 1, 6]),  # or [1, 6, 1, 5, 1, 4] etc.
        ([1, 3, 2, 2, 3, 1], [1, 3, 2, 2, 3, 1]),
        
        # All equal
        ([2, 2, 2, 2], [2, 2, 2, 2]),
        
        # Increasing
        ([1, 2, 3, 4], [1, 3, 2, 4]),
        
        # Decreasing
        ([4, 3, 2, 1], [3, 4, 1, 2]),
        
        # Single element
        ([10], [10]),
        
        # Empty
        ([], []),
    ]
    
    print("Testing Wiggle Sort\n" + "="*40)
    
    for idx, (nums, expected) in enumerate(test_cases, 1):
        sol = Solution()
        
        # Test both methods
        nums_copy1 = nums[:]
        sol.wiggleSort(nums_copy1)
        valid1 = is_wiggle(nums_copy1)
        
        nums_copy2 = nums[:]
        sol.wiggleSortLinear(nums_copy2)
        valid2 = is_wiggle(nums_copy2)
        
        print(f"Test {idx:2d}:")
        print(f"   Input:      {nums}")
        print(f"   Sorted + Swap: {nums_copy1} → Valid: {valid1}")
        print(f"   Linear:        {nums_copy2} → Valid: {valid2}")
        print("-" * 40)


def is_wiggle(arr: List[int]) -> bool:
    """Helper to verify wiggle property"""
    for i in range(1, len(arr)):
        if i % 2 == 1:
            if arr[i] <= arr[i - 1]:
                return False
        else:
            if arr[i] >= arr[i - 1]:
                return False
    return True


if __name__ == "__main__":
    run_tests()