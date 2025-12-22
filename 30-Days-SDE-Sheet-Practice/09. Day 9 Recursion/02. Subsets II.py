# https://leetcode.com/problems/subsets-ii/

# Use the same concept of 01. Subset Sums

# https://leetcode.com/problems/subsets-ii/

# Use the same concept of 01. Subset Sums (Include / Exclude)
# Sort the array to handle duplicates

class Solution:
    def subsetsWithDup(self, nums):
        nums.sort()
        res = []

        def dfs(i, subset):
            if i == len(nums):
                res.append(subset)
                return

            # Include current element
            dfs(i + 1, subset + [nums[i]])

            # Skip duplicates
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1

            # Exclude current element
            dfs(i + 1, subset)

        dfs(0, [])
        return res


# -------- DRIVER CODE --------
sol = Solution()

nums = [1, 2, 2]
print(sol.subsetsWithDup(nums))
# Expected Output: [[1, 2, 2], [1, 2], [1], [2, 2], [2], []]

nums = [0]
print(sol.subsetsWithDup(nums))
# Expected Output: [[0], []]

nums = [1, 1]
print(sol.subsetsWithDup(nums))
# Expected Output: [[1, 1], [1], []]


# Time: O(2^n)
# Space: O(2^n)  # as we are storeing subsets in path array in each calls