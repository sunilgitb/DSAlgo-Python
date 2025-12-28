# https://leetcode.com/problems/next-greater-element-i/

from typing import List
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        nextGreaterDic = {ch:-1 for ch in nums2}
        
        for i in range(len(nums2)):
            while stack and nums2[stack[-1]] < nums2[i]:
                nextGreaterDic[nums2[stack.pop()]] = nums2[i]
            stack.append(i)
        
        for i, ch in enumerate(nums1):
            nums1[i] = nextGreaterDic[ch]
        
        return nums1

# Example usage:
solution = Solution()
print(solution.nextGreaterElement([4,1,2], [1,3,4,2]))  # Output: [-1,3,-1]
print(solution.nextGreaterElement([2,4], [1,2,3,4]))    # Output: [3,-1]
        