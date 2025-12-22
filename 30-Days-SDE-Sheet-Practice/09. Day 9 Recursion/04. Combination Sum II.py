# https://leetcode.com/problems/combination-sum-ii/
''' 
At each index we have 2 options. Either keep the current element or skip the current element.
Make a recursion tree of this selection. We can select an element multiple times so one call 
with same index another call from next index.
'''
# https://leetcode.com/problems/combination-sum-ii/
''' 
Each number can be used ONLY ONCE.
Duplicates are present, so we must skip duplicate combinations.
At each index:
1) Pick current element and move to next index
2) Skip current element (skip all duplicates)
'''

class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()
        res = []

        def solve(i, target, path):
            if target == 0:
                res.append(path)
                return
            if i >= len(candidates) or target < 0:
                return

            # Pick current element (move to next index because one-time use)
            solve(i + 1, target - candidates[i], path + [candidates[i]])

            # Skip duplicates
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1

            # Skip current element
            solve(i + 1, target, path)

        solve(0, target, [])
        return res


# -------- DRIVER CODE --------
sol = Solution()

candidates = [10, 1, 2, 7, 6, 1, 5]
target = 8
print(sol.combinationSum2(candidates, target))
# Expected Output: [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]

candidates = [2, 5, 2, 1, 2]
target = 5
print(sol.combinationSum2(candidates, target))
# Expected Output: [[1, 2, 2], [5]]

candidates = [1, 1, 1]
target = 2
print(sol.combinationSum2(candidates, target))
# Expected Output: [[1, 1]]

# Time: O(2^N)
# Space: O(2^N)