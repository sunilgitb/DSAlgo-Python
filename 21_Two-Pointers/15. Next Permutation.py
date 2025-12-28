# https://leetcode.com/problems/next-permutation/
''' 
Next Permutation = elemtnt Just Greater than the current element.
So find the elemnt from traversing from end. if nums[i] > nums[i-1] we can swap these and get the 
value. but there may any greater element in right. 
'''

from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)

        # 1. Find first decreasing element from the right
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        # 2. If such element exists, find just larger element and swap
        if i >= 0:
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]

        # 3. Reverse the suffix
        nums[i + 1:] = reversed(nums[i + 1:])


if __name__ == "__main__":
    solution = Solution()

    nums = [1,2,3]
    solution.nextPermutation(nums)
    print(nums)
    # Output: [1, 3, 2]

    nums = [3,2,1]
    solution.nextPermutation(nums)
    print(nums)
    # Output: [1, 2, 3]

    nums = [1,1,5]
    solution.nextPermutation(nums)
    print(nums)
    # Output: [1, 5, 1]

    nums = [1,3,2]
    solution.nextPermutation(nums)
    print(nums)
    # Output: [2, 1, 3]

# Time: O(N)
# Space: O(1)
