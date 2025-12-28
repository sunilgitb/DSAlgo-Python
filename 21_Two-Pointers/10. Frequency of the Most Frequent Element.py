# https://leetcode.com/problems/frequency-of-the-most-frequent-element/


from typing import List

class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        prefixSum = []
        s = 0
        for i in nums:
            prefixSum.append(s)
            s += i
        
        res = 1
        l = 0
        for r in range(len(nums)):
            # check if we can make nums[l..r] all equal to nums[r] with <= k increments
            while nums[r] * (r - l) - (prefixSum[r] - prefixSum[l]) > k:
                l += 1
            res = max(res, r - l + 1)
        
        return res


if __name__ == "__main__":
    solution = Solution()
    
    nums = [3,9,6,5,2]
    k = 8
    print(solution.maxFrequency(nums, k))  # Output: 3
    
    nums = [1,2,4]
    k = 5
    print(solution.maxFrequency(nums, k))  # Output: 3
    
    nums = [1,4,8,13]
    k = 5
    print(solution.maxFrequency(nums, k))  # Output: 2

    
# Time: O(N)
# Space: O(N)
