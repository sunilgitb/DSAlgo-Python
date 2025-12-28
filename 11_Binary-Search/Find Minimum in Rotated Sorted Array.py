# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l = 0; r = n-1; res = nums[0]
        
        while l <= r:
            mid = l + (r - l) // 2
            res = min(res, nums[mid])
            if nums[l] <= nums[mid]:
                res = min(res, nums[l])
                l = mid + 1
            else:
                r = mid - 1

        return res
    
    
# Time: O(log(N))
# Space: O(1)

# Driver code:
solution = Solution()
print(solution.findMin([3,4,5,1,2]))  # Output: 1
print(solution.findMin([4,5,6,7,0,1,2]))  # Output: 0
print(solution.findMin([11,13,15,17]))  # Output: 11