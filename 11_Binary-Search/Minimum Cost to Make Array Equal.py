# https://leetcode.com/problems/minimum-cost-to-make-array-equal/

from typing import List
class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        def cal_cost(target):
            ans = 0
            for n, c in zip(nums, cost):
                ans += abs(target - n) * c
            return ans
        
        low = min(nums); high = max(nums)
        while low <= high:
            mid = low + (high - low) // 2
            cur_cost = cal_cost(mid)
            right_cost = cal_cost(mid + 1)
            
            if cur_cost < right_cost:
                high = mid - 1
            else:
                low = mid + 1
        
        return cal_cost(low)
      

# Time: O(N log(N))
# Space: O(1)
# Driver Code
solution = Solution()
print(solution.minCost([1,3,5,2], [2,3,1,14]))  # Output: 8
print(solution.minCost([2,2,2,2,2], [4,2,8,1,3]))  # Output: 0