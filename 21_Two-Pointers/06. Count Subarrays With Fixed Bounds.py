# https://leetcode.com/problems/count-subarrays-with-fixed-bounds/

from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        res = 0
        l = r = 0
        recentMin = recentMax = -1
        
        while r < len(nums):
            # Process valid subarray elements
            while r < len(nums) and minK <= nums[r] <= maxK:
                if nums[r] == minK:
                    recentMin = r
                if nums[r] == maxK:
                    recentMax = r
                if recentMin != -1 and recentMax != -1:
                    res += min(recentMin, recentMax) - l + 1
                r += 1
            
            # Reset window if invalid element found
            recentMin = recentMax = -1
            l = r + 1
            r += 1
        
        return res


if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    nums = [1,3,5,2,7,5]
    minK = 1
    maxK = 5
    print(solution.countSubarrays(nums, minK, maxK))  # Output: 2

    # Test case 2
    nums = [1,1,1,1]
    minK = 1
    maxK = 1
    print(solution.countSubarrays(nums, minK, maxK))  # Output: 10

    # Test case 3
    nums = [1,3,1,2,1,5,1]
    minK = 1
    maxK = 5
    print(solution.countSubarrays(nums, minK, maxK))  # Output depends on positions


    
# Time: O(N)
# Space: O(1)
