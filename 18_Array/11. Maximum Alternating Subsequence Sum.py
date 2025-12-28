# https://leetcode.com/problems/maximum-alternating-subsequence-sum/

from typing import List

class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        stack = []
        for num in nums:
            if not stack:
                stack.append(num)
            elif len(stack) % 2 == 1 and stack[-1] <= num:
                stack.pop()
                stack.append(num)
            elif len(stack) % 2 == 0 and stack[-1] >= num:
                stack.pop()
                stack.append(num)
            else:
                stack.append(num)

        # ensure odd length
        if len(stack) % 2 == 0:
            stack.pop()

        res = 0
        for i, val in enumerate(stack):
            res += val if i % 2 == 0 else -val

        return res

    
# Time: O(N)
# Space: O(N)



'''
Given an alternating sequence (a0, a1... ak), the change in value after appending an element x depends only on whether we have an even or odd number of elements so far:

If we have even # of elements, we add x; otherwise, we subtract x. So, tracking the best subsequences of odd and even sizes gives an extremely simple update formula.

'''
class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        odd = nums[0]
        even = 0

        for num in nums[1:]:
            odd = max(odd, even + num)
            even = max(even, odd - num)

        return max(odd, even)

# Time: O(N)
# Space: O(1)
solution = Solution()

print(solution.maxAlternatingSum([4, 2, 5, 3]))       # 7
print(solution.maxAlternatingSum([5, 6, 7, 8]))       # 8
print(solution.maxAlternatingSum([6, 2, 1, 2, 4, 5])) # 10
