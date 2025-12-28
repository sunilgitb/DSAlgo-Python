# https://leetcode.com/problems/maximum-erasure-value/


from typing import List

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        l = 0
        cur_sum = 0
        max_sum = 0
        seen = set()
        
        for r in range(len(nums)):
            while nums[r] in seen:
                seen.remove(nums[l])
                cur_sum -= nums[l]
                l += 1
            
            seen.add(nums[r])
            cur_sum += nums[r]
            max_sum = max(max_sum, cur_sum)
        
        return max_sum


if __name__ == "__main__":
    solution = Solution()
    
    nums = [4,2,4,5,6]
    print(solution.maximumUniqueSubarray(nums))
    # Output: 17
    # Explanation: Subarray [2,4,5,6] → sum = 17
    
    nums = [5,2,1,2,5,2,1,2,5]
    print(solution.maximumUniqueSubarray(nums))
    # Output: 8
    # Explanation: Subarray [5,2,1] or [1,2,5]
    
    nums = [100,1,2,3,4]
    print(solution.maximumUniqueSubarray(nums))
    # Output: 110

    
# Time: O(N)
# Space: O(N)
