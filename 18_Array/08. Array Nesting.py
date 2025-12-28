# https://leetcode.com/problems/array-nesting/description/


# https://leetcode.com/problems/array-nesting/

from typing import List

class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        res = 0
        visited = set()

        for i in range(len(nums)):
            if i in visited:
                continue

            count = 0
            cur = i
            while cur not in visited:
                visited.add(cur)
                cur = nums[cur]
                count += 1

            res = max(res, count)

        return res


# ---------------- DRIVER CODE ----------------
if __name__ == "__main__":
    solution = Solution()

    nums = [5, 4, 0, 3, 1, 6, 2]
    print(solution.arrayNesting(nums))   # Output: 4

    nums = [0, 1, 2]
    print(solution.arrayNesting(nums))   # Output: 1

    nums = [1, 0]
    print(solution.arrayNesting(nums))   # Output: 2



# Time: O(N)
# Space: O(N*N)
