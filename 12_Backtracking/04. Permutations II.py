# https://leetcode.com/problems/permutations-ii/

from typing import List
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        
        def dfs(arr, path):
            if not arr:
                res.append(path)
            for i in range(len(arr)):
                if i > 0 and arr[i] == arr[i-1]:
                    continue
                dfs(arr[:i] + arr[i+1:], path + [arr[i]])
            
        dfs(nums, [])
        return res

# Time: O(N^2)    # as for each element we are making (n-1) traversal again
# Space: O(N)     # as we are creating n-1 subarrays
# Space: O(N)     # as we are creating n-1 subarrays
# Example Usage:
sol = Solution()
print(sol.permuteUnique([1,1,2]))  # Output: [[1,1,2],[1,2,1],[2,1,1]]
print(sol.permuteUnique([1,2,3]))  # Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]