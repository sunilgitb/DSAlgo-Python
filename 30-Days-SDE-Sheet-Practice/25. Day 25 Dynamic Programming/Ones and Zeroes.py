# https://leetcode.com/problems/ones-and-zeroes/

# Method 1: Memoization(Top Down)
from typing import List
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        ZOCount = [(s.count('0'), s.count('1')) for s in strs]
        memo = {}
        
        def dfs(m, n, i):
            if m < 0 or n < 0: 
                return -2**31
            if i == len(ZOCount):
                return 0
            if (m, n, i) in memo: 
                return memo[(m, n, i)]
            zeros = ZOCount[i][0]
            ones = ZOCount[i][1]
            ans = max(1 + dfs(m - zeros, n - ones, i+1), dfs(m, n, i+1))
            memo[(m, n, i)] = ans
            return memo[(m, n, i)]
        
        return dfs(m, n, 0)
'''
Time: O(l * m * n) - where l is length of strs
Space: O(l * m * n) - memo hashmap
'''


# DP Tabulation (Bottom Up)
from typing import List
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0]*(n+1) for i in range(m+1)]
        
        for s in strs:
            zeros = s.count('0')
            ones = len(s) - zeros
            for i in range(m, zeros-1, -1):
                for j in range(n, ones-1, -1):
                    dp[i][j] = max(1 + dp[i-zeros][j-ones], dp[i][j])
        
        return dp[m][n]
    

'''
Time: O(l * m * n) - where l is length of strs
Space: O(m * n) - dp table
'''
# Example Usage
strs = ["10", "0001", "111001", "1", "0"]
m = 5
n = 3
sol = Solution()
print(sol.findMaxForm(strs, m, n))  # Output: 4   