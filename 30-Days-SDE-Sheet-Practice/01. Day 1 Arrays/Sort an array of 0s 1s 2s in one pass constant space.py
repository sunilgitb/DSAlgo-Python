# https://leetcode.com/problems/sort-colors/
# https://youtu.be/oaVa-9wmpns
'''
Dutch National Flag Algorithm:

Use 3 pointers named low, mid, and high to move 0s to the left and 
2s to the right and 1s in the middle of the array and hence the array will be sorted. 
'''

from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        low = 0
        mid = 0
        high = len(nums) - 1
        
        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:  # nums[mid] == 2
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1


# ---------------- DRIVER CODE ----------------
if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        [2, 0, 2, 1, 1, 0],
        [2, 0, 1],
        [0],
        [1],
        [2, 2, 1, 1, 0, 0],
        [0, 1, 2, 0, 1, 2]
    ]

    for idx, nums in enumerate(test_cases, 1):
        print(f"Test Case {idx}:")
        print("Before:", nums)
        sol.sortColors(nums)
        print("After: ", nums)
        print("-" * 30)


# Time: O(N)  # One Pass Solution
# Space: O(1)