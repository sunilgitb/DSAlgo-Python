# https://leetcode.com/problems/subsets-ii/

# -------------------------------------------- Method 1 ---------------------------------------------------------
from typing import List
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        
        def dfs(i, subset):
            if i >= len(nums):
                res.append(subset)
                return
            
            dfs(i+1, subset + [nums[i]])
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            dfs(i+1, subset)
        
        dfs(0, [])
        return res

# Driver Code:
solution = Solution()
print(solution.subsetsWithDup([1,2,2])) # Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
        
# Time: O(N * 2^N)
# Space: O(N)

# -------------------------------------------- Method 2 ---------------------------------------------------------
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        def dfs(i, subset):
            if i >= len(nums):
                res.add(tuple(subset))
                return
            dfs(i+1, subset + [nums[i]])
            dfs(i+1, subset)
        
        dfs(0, [])
        return res

# Driver Code:
solution = Solution()
print(solution.subsetsWithDup([1,2,2])) # Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]

# Time: O(N * 2^N)
# Space: O(N)
