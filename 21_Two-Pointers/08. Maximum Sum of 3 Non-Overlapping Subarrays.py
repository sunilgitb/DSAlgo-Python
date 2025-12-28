# https://leetcode.com/problems/maximum-sum-of-3-non-overlapping-subarrays/
# https://youtu.be/mXeT7-oZeQQ

'''
First Solve: Maximum Sum of Two Non-Overlapping Subarrays

move a window of size k between left and right parts and check maxsum
'''

class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        prefixSum = []
        s = 0
        for i in nums:
            s += i
            prefixSum.append(s)

        n = len(nums)
        left = [(0,0)] * n
        for i in range(k-1, n-2*k):
            curSum = prefixSum[i] - prefixSum[i-k+1] + nums[i-k+1]
            if i>0: left[i] = left[i-1]
            if curSum > left[i][0]:
                left[i] = (curSum, i-k+1)
        
        right = [(0,0)] * n
        for i in range(n-k, 2*k-1, -1):
            curSum = prefixSum[i+k-1] - prefixSum[i] + nums[i]
            if i+1 < n: right[i] = right[i+1]
            if curSum >= right[i][0]:
                right[i] = (curSum, i)
        
        res = []
        maxSum = 0
        for i in range(k, n-k):
            l = i-1
            r = i+k
            curSum = left[l][0] + (prefixSum[r-1] - prefixSum[l]) + right[r][0]
            if curSum > maxSum:
                maxSum = curSum
                res = [left[l][1], i, right[r][1]]
        # print(prefixSum)
        # print(left)
        # print(right)
        return res
        
                
            
# Time: O(N)
# Space: O(N)
from typing import List

class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        # compute prefix sums
        prefixSum = [0] * n
        s = 0
        for i, num in enumerate(nums):
            s += num
            prefixSum[i] = s

        # max sum subarray of length k ending at or before i
        left = [(0,0)] * n
        for i in range(k-1, n):
            curSum = prefixSum[i] - (prefixSum[i-k] if i-k >= 0 else 0)
            if i > 0:
                left[i] = left[i-1]
            if curSum > left[i][0]:
                left[i] = (curSum, i-k+1)
        
        # max sum subarray of length k starting at or after i
        right = [(0,0)] * n
        for i in range(n-k, -1, -1):
            curSum = prefixSum[i+k-1] - (prefixSum[i-1] if i-1 >= 0 else 0)
            if i+1 < n:
                right[i] = right[i+1]
            if curSum >= right[i][0]:
                right[i] = (curSum, i)
        
        # middle subarray
        maxSum = 0
        res = []
        for mid in range(k, n-2*k+1):
            l_sum, l_idx = left[mid-1]
            m_sum = prefixSum[mid+k-1] - prefixSum[mid-1]
            r_sum, r_idx = right[mid+k]
            total = l_sum + m_sum + r_sum
            if total > maxSum:
                maxSum = total
                res = [l_idx, mid, r_idx]
        
        return res


if __name__ == "__main__":
    solution = Solution()
    
    nums = [1,2,1,2,6,7,5,1]
    k = 2
    print(solution.maxSumOfThreeSubarrays(nums, k))  # Output: [0, 3, 5]

    nums = [4,5,10,6,11,17,4,3,2,9,10,1]
    k = 3
    print(solution.maxSumOfThreeSubarrays(nums, k))  # Output will be indices of the 3 subarrays
