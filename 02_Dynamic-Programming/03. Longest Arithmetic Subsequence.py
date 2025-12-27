from typing import List

class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        dp = [{} for _ in range(len(nums))]
        res = 0
        
        for i in range(len(nums)):
            for j in range(i):
                diff = nums[i] - nums[j]
                dp[i][diff] = dp[j].get(diff, 1) + 1
                res = max(res, dp[i][diff])
        
        return res


# Test cases
solution = Solution()

# Test 1
nums1 = [3,6,9,12]
print("Test 1:", solution.longestArithSeqLength(nums1))  # Expected: 4

# Test 2
nums2 = [9,4,7,2,10]
print("Test 2:", solution.longestArithSeqLength(nums2))  # Expected: 3

# Test 3
nums3 = [20,1,15,3,10,5,8]
print("Test 3:", solution.longestArithSeqLength(nums3))  # Expected: 4

# Test 4
nums4 = [83,20,17,43,52,78,68,45]
print("Test 4:", solution.longestArithSeqLength(nums4))  # Expected: 2

# Test 5
nums5 = [44,46,22,68,45,66,43,9,37,30,50,67,32,47,44,11,15,4,11,6,20,64,54,54,61,63,23,43,3,12,51,61,16,57,14,12,55,17,18,25,19,28,45,56,29,39,52,8,1,21,17,21,23,70,51,61,21,52,25,28]
print("Test 5:", solution.longestArithSeqLength(nums5))  # Expected: 6