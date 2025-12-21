# https://leetcode.com/problems/3sum/

# https://leetcode.com/problems/3sum/

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i, ch in enumerate(nums):
            # skip duplicate fixed elements
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = ch + nums[l] + nums[r]

                if threeSum < 0:
                    l += 1
                elif threeSum > 0:
                    r -= 1
                else:
                    res.append([ch, nums[l], nums[r]])
                    l += 1

                    # skip duplicate left values
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

        return res


# ---------------- DRIVER CODE ----------------
if __name__ == "__main__":
    sol = Solution()

    nums = [-1, 0, 1, 2, -1, -4]
    result = sol.threeSum(nums)

    print(result)
    # Expected Output:
    # [[-1, -1, 2], [-1, 0, 1]]



# Time: O(N^2)
# Space: O(1)