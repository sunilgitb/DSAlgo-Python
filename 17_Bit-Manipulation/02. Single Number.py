# https://leetcode.com/problems/single-number/

# https://leetcode.com/problems/single-number/

from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        '''
        XOR logic:
        (4 XOR 3) XOR 3 = 4
        - xor of same number = 0; so 3^3 = 0
        - xor of any number with 0 equals that number
        => 4^3^3 = 4
        '''
        res = 0
        for i in nums:
            res ^= i  # twice numbers cancel out, leaving the single number
        return res


# -------- Driver Code --------
solution = Solution()

print(solution.singleNumber([2,2,1]))          # 1
print(solution.singleNumber([4,1,2,1,2]))      # 4
print(solution.singleNumber([1]))              # 1
print(solution.singleNumber([17,5,5,17,23]))   # 23

# Time: O(N)
# Space: O(1)
    
'''
        return 2 * sum(set(nums)) - sum(nums)

Time: O(N)  # as sum() internally use a loop
Space: O(N) # for making set of nums
'''