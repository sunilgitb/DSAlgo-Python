# https://leetcode.com/problems/sliding-window-maximum/

from typing import List
import collections
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = collections.deque()
        res = []
        
        for i in range(len(nums)):
            while q and nums[i] >= nums[q[-1]]:
                q.pop()
                
            if q and i - q[0] >= k:
                q.popleft()
                
            q.append(i)
            
            if i >= k-1: res.append(nums[q[0]])
        
        return res
            
# Driver Code:
solution = Solution()
nums = [1,3,-1,-3,5,3,6,7]
k = 3
print(solution.maxSlidingWindow(nums, k))  # Output: [3,3,5,5,6,7]
# Time: O(N)
# Space: O(N)

''' 
The time complexity of deque.popleft() is O(1),
while the time complexity of list.pop(0) is O(k), as index 0 is considered an intermediate index.
'''