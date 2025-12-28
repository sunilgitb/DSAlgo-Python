# https://leetcode.com/problems/total-hamming-distance/
'''
Notice the total hamming distance is the sum of the total hamming distance for each of the i-th bits separately.

Total hamming distance for the i-th bit = 
(the number of zeros in the i-th position) * (the number of ones in the i-th position).

We then add all of these together to get our answer.
'''

from typing import List
class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        res = 0
        for i in range(32):
            mask = 1 << i
            zero = 0
            one = 0
            for num in nums:
                if num & mask:
                    one += 1
                else:
                    zero += 1
            res += zero * one
        return res


# -------- Driver Code --------
solution = Solution()

print(solution.totalHammingDistance([4, 14, 2]))      # 6
print(solution.totalHammingDistance([1, 2, 3]))       # 4
print(solution.totalHammingDistance([0, 0, 0]))       # 0
print(solution.totalHammingDistance([1, 1, 1, 0]))    # 3


# Time: O(N) ; where N = len(nums)
# Space: O(1); not using any extra data structure