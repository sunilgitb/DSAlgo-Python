# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
''' 
take 2 pointers prev and cur. prev will only increase for different values. so the resulting array 
will be of unique value.
'''
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev = 0
        
        for i in range(1, len(nums)):
            if nums[prev] != nums[i]:
                prev += 1
                nums[prev] = nums[i]
        
        return prev + 1


# ---------------- DRIVER CODE ----------------
if __name__ == "__main__":
    sol = Solution()

    nums = [1, 1, 2]
    k = sol.removeDuplicates(nums)
    print(k)
    # Expected Output: 2
    print(nums[:k])
    # Expected Output: [1, 2]

    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    k = sol.removeDuplicates(nums)
    print(k)
    # Expected Output: 5
    print(nums[:k])
    # Expected Output: [0, 1, 2, 3, 4]

    nums = [1, 1, 1, 1]
    k = sol.removeDuplicates(nums)
    print(k)
    # Expected Output: 1
    print(nums[:k])
    # Expected Output: [1]


# Time: O(n)
# Space: O(1)