# https://leetcode.com/problems/combination-sum/
''' 
At each index we have 2 options. Either keep the current element or skip the current element.
Make a recursion tree of this selection. We can select an element multiple times so one call 
with same index another call from next index.
'''
# https://leetcode.com/problems/combination-sum/
# Combination Sum - Find all unique combinations that sum to target
# (Elements can be used unlimited times)

from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        def solve(i: int, remaining: int, path: List[int]):
            # Base cases
            if remaining == 0:
                res.append(path[:])  # Found a valid combination
                return
            if remaining < 0 or i >= len(candidates):
                return
            
            # 1. Take the current candidate (can take it again later)
            solve(i, remaining - candidates[i], path + [candidates[i]])
            
            # 2. Skip the current candidate (move to next)
            solve(i + 1, remaining, path)
        
        solve(0, target, [])
        return res


# ──────────────────────────────────────────────────────────────
# Driver Code (for local testing)
# ──────────────────────────────────────────────────────────────

if __name__ == "__main__":
    sol = Solution()

    # Test Case 1
    candidates1 = [2, 3, 6, 7]
    target1 = 7
    result1 = sol.combinationSum(candidates1, target1)
    print("Input: candidates =", candidates1, "target =", target1)
    print("Output:")
    for comb in sorted(result1):
        print(comb)
    # Expected:
    # [2,2,3]
    # [7]

    print("-" * 50)

    # Test Case 2
    candidates2 = [2, 3, 5]
    target2 = 8
    result2 = sol.combinationSum(candidates2, target2)
    print("Input: candidates =", candidates2, "target =", target2)
    print("Output:")
    for comb in sorted(result2):
        print(comb)
    # Expected:
    # [2,2,2,2]
    # [2,3,3]
    # [3,5]

    print("-" * 50)

    # Test Case 3
    candidates3 = [2]
    target3 = 1
    result3 = sol.combinationSum(candidates3, target3)
    print("Input: candidates =", candidates3, "target =", target3)
    print("Output:", result3)  # []
        
# Time and space complexity of this problem if not fixed. But below is the hypothetical time and space
# Time: O(2^t * n) ; where t = target/candidate[i] ; n = len(candidates)
# Space: O(nCk)  ; where n = len(candidates) ; k = number of combinations
# k depends on the values of candidates as if large value more quickly target can be achived and less length
