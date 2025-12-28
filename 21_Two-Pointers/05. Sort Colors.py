# https://leetcode.com/problems/sort-colors/
# https://youtu.be/oaVa-9wmpns
'''
Dutch National Flag Algorithm:

Use 3 pointers named low, mid, and high to move 0s to the left and 2s to the right and 1s in the middle of the array and hence the array will be sorted. 
'''

from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> List[int]:
        left, mid = 0, 0
        right = len(nums) - 1
        
        while mid <= right:
            if nums[mid] == 0:
                nums[left], nums[mid] = nums[mid], nums[left]
                left += 1
                mid += 1
            elif nums[mid] == 2:
                nums[mid], nums[right] = nums[right], nums[mid]
                right -= 1
            else:  # nums[mid] == 1
                mid += 1
        
        return nums


if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1
    nums = [2,0,2,1,1,0]
    print("Before:", nums)
    print("After: ", solution.sortColors(nums))  # Output: [0,0,1,1,2,2]

    # Test Case 2
    nums = [2,0,1]
    print("\nBefore:", nums)
    print("After: ", solution.sortColors(nums))  # Output: [0,1,2]

    # Test Case 3
    nums = [0]
    print("\nBefore:", nums)
    print("After: ", solution.sortColors(nums))  # Output: [0]

    # Test Case 4
    nums = [1]
    print("\nBefore:", nums)
    print("After: ", solution.sortColors(nums))  # Output: [1]


# Time: O(N)  # One Pass Solution
# Space: O(1)

