# https://leetcode.com/problems/permutations/

from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def solve(nums, path):
            if not nums: 
                res.append(path)
                return
            
            for i in range(len(nums)):
                solve(nums[:i] + nums[i+1:], path + [nums[i]])
            
        solve(nums, [])
        return res

# Time: (n * n!) # as we are generating each pernutation and traversing the array
# Space: O(n!)   # n factorial as we are generating each permutation


if __name__ == '__main__':
    sol = Solution()
    tests = [[1, 2, 3], [0, 1], [], [1]]

    for nums in tests:
        res = sol.permute(nums)
        print(f"\nnums = {nums} -> {len(res)} permutation(s)")
        for idx, p in enumerate(res, 1):
            print(f"Perm {idx}: {p}")
