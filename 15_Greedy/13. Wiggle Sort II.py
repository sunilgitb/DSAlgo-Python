# https://leetcode.com/problems/wiggle-sort-ii/
# Wiggle Sort II
# Problem: Rearrange nums such that nums[0] < nums[1] > nums[2] < nums[3] > ...
#          and the difference between consecutive elements is maximized
#          (strictly greater/smaller than neighbors).

from typing import List


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        O(n log n) time, O(n) space (using extra array)
        Approach:
        - Sort the array
        - Place smaller half into even indices (0, 2, 4, ...)
        - Place larger half into odd indices (1, 3, 5, ...)
        - Ensures strict < > < > pattern with maximum possible difference
        """
        n = len(nums)
        if n <= 1:
            return

        # Step 1: Sort the array
        arr = sorted(nums)

        # Step 2: Split into smaller and larger halves
        mid = (n + 1) // 2  # length of smaller half

        # Step 3: Fill even indices with smaller half (reversed)
        for i in range(mid):
            nums[2 * i] = arr[i]

        # Step 4: Fill odd indices with larger half (reversed)
        for i in range(n - mid):
            nums[2 * i + 1] = arr[mid + i]


    def wiggleSortInPlace(self, nums: List[int]) -> None:
        """
        O(n log n) time, O(1) extra space (but modifies original array)
        Similar to your approach but correctly handles placement
        """
        n = len(nums)
        if n <= 1:
            return

        # Sort a copy
        arr = sorted(nums)

        # Place largest elements into odd indices (from back)
        j = n - 1  # start from largest
        for i in range(1, n, 2):
            nums[i] = arr[j]
            j -= 1

        # Place remaining (smaller) elements into even indices
        for i in range(0, n, 2):
            nums[i] = arr[j]
            j -= 1


# Driver Code with test cases
def run_tests():
    test_cases = [
        # Example 1
        ([1, 5, 1, 1, 6, 4], [1, 6, 1, 5, 1, 4]),  # or [1, 4, 1, 5, 1, 6] etc.

        # Example 2
        ([1, 3, 2, 2, 3, 1], [1, 3, 2, 2, 3, 1]),

        # All equal
        ([1, 1, 1, 1], [1, 1, 1, 1]),

        # Increasing
        ([1, 2, 3, 4], [1, 3, 2, 4]),

        # Single element
        ([5], [5]),

        # Two elements
        ([1, 2], [1, 2]),
    ]

    print("Testing Wiggle Sort II\n" + "="*50)

    for idx, (nums, expected) in enumerate(test_cases, 1):
        sol = Solution()
        nums_copy = nums[:]
        sol.wiggleSort(nums_copy)
        valid = is_valid_wiggle(nums_copy)

        print(f"Test {idx:2d}:")
        print(f"   Input:     {nums}")
        print(f"   Output:    {nums_copy}")
        print(f"   Valid:     {valid}")
        print("-" * 50)


def is_valid_wiggle(arr: List[int]) -> bool:
    """Check if array satisfies nums[0] < nums[1] > nums[2] < nums[3] > ..."""
    for i in range(1, len(arr)):
        if i % 2 == 1:
            if arr[i] <= arr[i-1]:
                return False
        else:
            if arr[i] >= arr[i-1]:
                return False
    return True


if __name__ == "__main__":
    run_tests()