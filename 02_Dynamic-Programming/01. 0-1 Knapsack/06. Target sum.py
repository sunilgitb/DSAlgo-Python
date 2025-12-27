# https://www.youtube.com/watch?v=Hw6Ygp3JBYw&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=12
# https://leetcode.com/problems/target-sum/
'''
Assigning + and - before elements of nums such that sum of all elements is equal to target
Basically we are again deviding the array into 2 subsets such that diffrence between that subsets equal to target
s1 - s2 = target    ---(1)
s1 + s2 = sum(nums) ---(2)
(1) + (2)
s1 = (target + sum(nums)) // 2
Now we have to find number of possible subsets s1 in nums
'''

from typing import List

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)

        # Impossible cases
        if abs(target) > total:
            return 0
        if (total + target) % 2 != 0:
            return 0

        s1 = (total + target) // 2
        n = len(nums)

        dp = [[0] * (s1 + 1) for _ in range(n + 1)]

        # Base case: sum = 0 → 1 way (empty subset)
        dp[0][0] = 1

        for i in range(1, n + 1):
            for j in range(s1 + 1):
                if nums[i - 1] <= j:
                    dp[i][j] = dp[i - 1][j] + dp[i - 1][j - nums[i - 1]]
                else:
                    dp[i][j] = dp[i - 1][j]

        return dp[n][s1]


# Time Complexity: O(n * s1)
# Space Complexity: O(n * s1)


# -------- Example Usage --------
sol = Solution()

print(sol.findTargetSumWays([1,1,1,1,1], 3))
# Expected Output: 5

print(sol.findTargetSumWays([1], 1))
# Expected Output: 1

print(sol.findTargetSumWays([0,0,0,0,0], 0))
# Expected Output: 32




#Memoization (Top-down) approach

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:    
        def dfs(i,tgt):
        # Base case: if we have reached the end of the list
            if i==0:
                if tgt==0:
                    return 1
                else:
                    return 0
            if (i,tgt) in dp:
                return dp[(i,tgt)] 
            if nums[i]<=tgt:
                pick=dfs(i-1,tgt-nums[i])
            not_pick=dfs(i-1,tgt)

            dp[(i,tgt)]=pick+not_pick
        

            return dp[(i,tgt)]
        
        if (sum(nums)+target)%2==0:
         # Create a memoization dictionary
            dp={}
            tgt=(sum(nums)+target)//2
            return dfs(len(nums)-1,tgt)
        else:
            return 0