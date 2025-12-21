# https://leetcode.com/problems/max-consecutive-ones/

''' 
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        i = 0
        while i < len(nums):
            count = 0
            while i < len(nums) and nums[i] == 1:
                count += 1
                i += 1
            res = max(res, count)
            i += 1
        
        return res
            
# Time: O(n)
# Space: O(1)
'''

# https://leetcode.com/problems/max-consecutive-ones/

from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        tmp = 0
        
        for num in nums:
            if num == 0:
                tmp = 0
            else:
                tmp += 1
                res = max(res, tmp)
        
        return res


# ---------------- DRIVER CODE ----------------
if __name__ == "__main__":
    sol = Solution()

    nums = [1, 1, 0, 1, 1, 1]
    print(sol.findMaxConsecutiveOnes(nums))
    # Expected Output: 3

    nums = [1, 0, 1, 1, 0, 1]
    print(sol.findMaxConsecutiveOnes(nums))
    # Expected Output: 2

    nums = [0, 0, 0, 0]
    print(sol.findMaxConsecutiveOnes(nums))
    # Expected Output: 0

    nums = [1, 1, 1, 1]
    print(sol.findMaxConsecutiveOnes(nums))
    # Expected Output: 4


# Time: O(N)
# Space: O(1)