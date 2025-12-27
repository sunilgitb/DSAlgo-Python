# https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n+1)
        dp[0] = dp[1] = 1
        
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[n]
    
# Time: O(n)
# Space: O(n)
sol = Solution()

print(sol.climbStairs(2))  # Output: 2
# Explanation: (1+1), (2)

print(sol.climbStairs(3))  # Output: 3
# Explanation: (1+1+1), (1+2), (2+1)

print(sol.climbStairs(5))  # Output: 8
