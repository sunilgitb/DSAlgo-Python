# https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/

from typing import List

class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        # Sort the array to find the median
        nums.sort()
        median = nums[len(nums) // 2]  # Median minimizes the sum of absolute differences
        ans = sum(abs(median - num) for num in nums)
        return ans

# ---------------- Driver Code ----------------
if __name__ == "__main__":
    nums = [1, 2, 3]
    solution = Solution()
    print("Minimum moves:", solution.minMoves2(nums))  # Output: 2
