# https://leetcode.com/problems/combination-sum/
''' 
At each index we have 2 options. Either keep the current element or skip the current element.
Make a recursion tree of this selection. We can select an element multiple times so one call 
with same index another call from next index.
'''
# https://leetcode.com/problems/combination-sum/
''' 
At each index we have 2 options:
1) Pick the current element (can be picked multiple times)
2) Skip the current element and move to next index

This forms a recursion tree.
'''

class Solution:
    def combinationSum(self, candidates, target):
        res = []

        def solve(i, target, path):
            if target == 0:
                res.append(path)
                return
            if target < 0 or i >= len(candidates):
                return

            # Pick current element (stay at same index)
            solve(i, target - candidates[i], path + [candidates[i]])

            # Skip current element (move to next index)
            solve(i + 1, target, path)

        solve(0, target, [])
        return res


# -------- DRIVER CODE --------
sol = Solution()

candidates = [2, 3, 6, 7]
target = 7
print(sol.combinationSum(candidates, target))
# Expected Output: [[2, 2, 3], [7]]

candidates = [2, 3, 5]
target = 8
print(sol.combinationSum(candidates, target))
# Expected Output: [[2, 2, 2, 2], [2, 3, 3], [3, 5]]

candidates = [2]
target = 1
print(sol.combinationSum(candidates, target))
# Expected Output: []

        
# Time and space complexity of this problem if not fixed. But below is the hypothetical time and space
# Time: O(2^t * n) ; where t = target/candidate[i] ; n = len(candidates)
# Space: O(nCk)  ; where n = len(candidates) ; k = number of combinations
# k depends on the values of candidates as if large value more quickly target can be achived and less length
