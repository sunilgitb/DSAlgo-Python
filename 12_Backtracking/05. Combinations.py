# https://leetcode.com/problems/combinations/
# https://youtu.be/q0s6m7AiM7o

from typing import List
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        
        def dfs(start, comb):
            if len(comb) >= k:
                res.append(comb)
                return
            for i in range(start, n+1):
                dfs(i+1, comb + [i])
        
        dfs(1, [])
        return res
# Example usage:
sol = Solution()
print(sol.combine(4, 2))  # Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]