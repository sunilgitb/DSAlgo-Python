# https://leetcode.com/problems/fair-distribution-of-cookies/

from typing import List
class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        self.res = 2**31
        children = [0] * k
        def dfs(i):
            if i >= len(cookies):
                self.res = min(self.res, max(children))
                return
            if max(children) > self.res: return
            for j in range(k):
                children[j] += cookies[i]
                dfs(i+1)
                children[j] -= cookies[i]
                
        dfs(0)
        return self.res

# Time: O(n^k)
# Space: O(k)

# Example usage:
sol = Solution()
print(sol.distributeCookies([8,15,10,20,8], 2))  # Output: 31
print(sol.distributeCookies([6,1,3,2,2,4,1,2], 3))  # Output: 7
