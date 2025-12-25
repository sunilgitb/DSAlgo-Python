# https://leetcode.com/problems/next-greater-element-i/
from typing import List
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        nextGreaterDic = {ch:-1 for ch in nums2}
        
        for i in range(len(nums2)):
            # Maintain a decreasing stack of indices of nums2 elements
            while stack and nums2[stack[-1]] < nums2[i]:
                # Pop from stack and set the next greater element in the dictionary
                nextGreaterDic[nums2[stack.pop()]] = nums2[i]
            # Push current index onto the stack
            stack.append(i)
        # Map the results back to nums1
        for i, ch in enumerate(nums1):
            # Replace each element in nums1 with its next greater element from the dictionary
            nums1[i] = nextGreaterDic[ch]

        return nums1

# Example usage:
solution = Solution()
print(solution.nextGreaterElement([4,1,2], [1,3,4,2]))  # Output: [-1,3,-1]
print(solution.nextGreaterElement([2,4], [1,2,3,4]))    # Output: [3,-1]