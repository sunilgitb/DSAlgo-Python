# https://leetcode.com/problems/remove-element/

from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        for num in nums:
            if num != val:
                nums[i] = num
                i += 1
        return i


if __name__ == "__main__":
    solution = Solution()
    
    nums = [3,2,2,3]
    val = 3
    k = solution.removeElement(nums, val)
    print(f"New length: {k}, Array after removal: {nums[:k]}")  # Output: New length: 2, Array: [2,2]
    
    nums = [0,1,2,2,3,0,4,2]
    val = 2
    k = solution.removeElement(nums, val)
    print(f"New length: {k}, Array after removal: {nums[:k]}")  # Output: New length: 5, Array: [0,1,3,0,4]
