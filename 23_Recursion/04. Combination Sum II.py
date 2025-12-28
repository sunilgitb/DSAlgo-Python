# https://leetcode.com/problems/combination-sum-ii/
''' 
At each index we have 2 options. Either keep the current element or skip the current element.
Make a recursion tree of this selection. We can select an element multiple times so one call 
with same index another call from next index.
'''
# https://leetcode.com/problems/combination-sum-ii/
# Combination Sum II - Find all unique combinations that sum to target
# (Elements can be used ONLY ONCE, duplicates in input)

from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()  # Sort to handle duplicates
        res = []
        
        def solve(i: int, remaining: int, path: List[int]):
            # Base cases
            if remaining == 0:
                res.append(path[:])  # Found a valid combination
                return
            if i >= len(candidates) or remaining < 0:
                return
            
            # 1. Take the current candidate (move to next index - used only once)
            solve(i + 1, remaining - candidates[i], path + [candidates[i]])
            
            # 2. Skip duplicates AND the current element
            # Skip all identical elements to avoid duplicate combinations
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            solve(i + 1, remaining, path)
        
        solve(0, target, [])
        return res


# ──────────────────────────────────────────────────────────────
# Driver Code (for local testing)
# ──────────────────────────────────────────────────────────────

if __name__ == "__main__":
    sol = Solution()

    # Test Case 1
    candidates1 = [10, 1, 2, 7, 6, 1, 5]
    target1 = 8
    result1 = sol.combinationSum2(candidates1, target1)
    print("Input: candidates =", candidates1, "target =", target1)
    print("Output:")
    for comb in sorted(result1):
        print(comb)
    # Expected (after sorting candidates: [1,1,2,5,6,7,10]):
    # [1, 1, 6]
    # [1, 2, 5]
    # [1, 7]
    # [2, 6]

    print("-" * 50)

    # Test Case 2
    candidates2 = [2, 5, 2, 1, 2]
    target2 = 5
    result2 = sol.combinationSum2(candidates2, target2)
    print("Input: candidates =", candidates2, "target =", target2)
    print("Output:")
    for comb in sorted(result2):
        print(comb)
    # Expected (after sorting: [1,2,2,2,5]):
    # [1, 2, 2]
    # [2, 2, 1]  # Same as above but different order - prevented by sorting
    # [5]

    print("-" * 50)

    # Test Case 3 (with duplicates that don't form target)
    candidates3 = [3, 1, 3, 3]
    target3 = 7
    result3 = sol.combinationSum2(candidates3, target3)
    print("Input: candidates =", candidates3, "target =", target3)
    print("Output:", sorted(result3))  # []
# Time: O(2^N)
# Space: O(2^N)