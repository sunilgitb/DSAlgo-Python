# https://leetcode.com/problems/smallest-subarrays-with-maximum-bitwise-or/

'''
# Intuition
Assume the array has only 0 and 1.
Then the question changes:
If A[i] = 1, shortest array is [A[i]], length is 1.
If A[i] = 0, we need to find the index j of next 1,
then j - i + 1 is the length of shortest subarray.
If no next 1, 1 is the length

To solve this problem,
we can iterate the array reversely
and keep the index j of last time we saw 1.
res[i] = max(1, last - i + 1)
'''


from typing import List

class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        n = len(nums)
        lastIndex = [0] * 32   # last index where each bit is set
        res = [1] * n
        
        for i in range(n-1, -1, -1):
            for j in range(32):
                if nums[i] & (1 << j):
                    lastIndex[j] = i
            res[i] = max(1, max(lastIndex) - i + 1)
        
        return res


# -------- Driver Code --------
solution = Solution()

print(solution.smallestSubarrays([1, 0, 2, 1, 3]))   # [3,3,2,2,1]
print(solution.smallestSubarrays([4, 3, 2, 1]))      # [1,2,3,4]
print(solution.smallestSubarrays([0,0,0]))          # [1,1,1]
print(solution.smallestSubarrays([1,2,4,8]))        # [4,3,2,1]

    
    
    
    
# Time: O(N)
# Space: O(N)
