# https://leetcode.com/problems/maximum-subarray/
''' 
continuously adding new elements to cs and also checking if the current value is greater or not.
if greater then start from current element.
'''

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Kadane's Algorithm
        cs = 0
        ms = nums[0]

        for num in nums:
            cs += num
            cs = max(cs, num)
            ms = max(ms, cs)

        return ms


# ---------------- DRIVER CODE ----------------
if __name__ == "__main__":
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    # Expected Output: 6 (subarray [4, -1, 2, 1])

    sol = Solution()
    result = sol.maxSubArray(nums)
    print("Maximum Subarray Sum:", result)


# Time: O(N)
# Spave: O(1)