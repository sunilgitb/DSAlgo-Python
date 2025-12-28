# https://leetcode.com/problems/132-pattern/
# https://youtu.be/q5ANAl8Z458

from typing import List
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        curMin = nums[0]
        stack = []  # stack contains [nums[i], nums[j]] and n = nums[k] 
        
        for n in nums[1:]:
            while stack and n >= stack[-1][1]:
                stack.pop()
            if stack and n > stack[-1][0]: 
                return True
            stack.append([curMin, n])
            curMin = min(curMin, n)
        
        return False

# Example usage:
sol = Solution()
print(sol.find132pattern([1, 2, 3, 4]))  # Output: False
print(sol.find132pattern([3, 1, 4, 2]))  # Output: True
print(sol.find132pattern([-1, 3, 2, 0]))  # Output: True
      
      
