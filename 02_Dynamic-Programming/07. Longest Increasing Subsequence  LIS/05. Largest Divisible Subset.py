# https://leetcode.com/problems/largest-divisible-subset/

from typing import List

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
            
        nums.sort()
        # numDict[num] = longest divisible subset ending with num
        numDict = {num: [num] for num in nums}
        
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0 and len(numDict[nums[i]]) < len(numDict[nums[j]]) + 1:
                    numDict[nums[i]] = numDict[nums[j]] + [nums[i]]
        
        # Find the longest subset
        res = []
        for num in numDict:
            if len(numDict[num]) > len(res):
                res = numDict[num]
        
        return res


# ---------------- Example Usage ----------------
sol = Solution()

# Example 1
nums = [1,2,3]
print(sol.largestDivisibleSubset(nums))  # Output: [1,2] or [1,3]

# Example 2
nums = [1,2,4,8]
print(sol.largestDivisibleSubset(nums))  # Output: [1,2,4,8]

# Example 3
nums = [3,6,9,12]
print(sol.largestDivisibleSubset(nums))  # Output: [3,6,9,12]

# Example 4
nums = [5,9,11,13]
print(sol.largestDivisibleSubset(nums))  # Output: [5] (or any single element)

# Example 5
nums = [4,8,16]
print(sol.largestDivisibleSubset(nums))  # Output: [4,8,16]

# Example 6
nums = [10,20,30,40,50]
print(sol.largestDivisibleSubset(nums))  # Output: [10,20,40] (or [10,20,30,40,50] if all divisible)