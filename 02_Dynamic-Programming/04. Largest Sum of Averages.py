from typing import List

class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        dp = [[-1] * (k+1) for _ in range(len(nums))]
        
        def dfs(i, k):
            if i >= len(nums) or k < 0: 
                return 0
            if k == 0: 
                return -2**31
            if dp[i][k] != -1: 
                return dp[i][k]
            
            ans = 0
            s = 0
            for j in range(i, len(nums)):
                s += nums[j]
                ans = max(ans, s/(j-i+1) + dfs(j+1, k-1))
            
            dp[i][k] = ans
            return ans
        
        return dfs(0, k)


# Test cases
solution = Solution()

# Test 1
nums1 = [9,1,2,3,9]
k1 = 3
print("Test 1:", solution.largestSumOfAverages(nums1, k1))  # Expected: 20.0

# Test 2
nums2 = [1,2,3,4,5,6,7]
k2 = 4
print("Test 2:", solution.largestSumOfAverages(nums2, k2))  # Expected: 20.5

# Test 3
nums3 = [4,1,7,5,6,2,3]
k3 = 4
print("Test 3:", solution.largestSumOfAverages(nums3, k3))  # Expected: 18.16667