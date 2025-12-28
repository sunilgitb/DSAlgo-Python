# https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

from typing import List
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # First Solve => Allocate Minimum Number Of Pages - Binary Search
        
        l = max(weights);  r = sum(weights);  ans = -1
        
        if len(weights) < days: return -1
        
        def isValid(weight, days, mid):
            currSumWt = 0
            countOfDays = 1
            for wt in weights:
                currSumWt += wt
                if currSumWt > mid:
                    countOfDays += 1
                    currSumWt = wt
            if countOfDays > days: return False
            else: return True
        
        while l <= r:
            mid = (l+r) // 2
            if isValid(weights, days, mid):
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        
        return ans
# Time Complexity: O(N log(sum of weights))
# Space Complexity: O(1)

# Example Usage
sol = Solution()
print(sol.shipWithinDays([1,2,3,4,5,6,7,8,9,10], 5))  # Output: 15
print(sol.shipWithinDays([3,2,2,4,1,4], 3))          # Output: 6
print(sol.shipWithinDays([1,2,3,1,1], 4))          # Output: 3