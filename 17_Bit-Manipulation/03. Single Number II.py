# https://leetcode.com/problems/single-number-ii/

from typing import List

class Solution:
    # Bit manipulation: count each bit modulo 3
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for i in range(32):
            s = 0
            for num in nums:
                if (num >> i) & 1:
                    s += 1
            s %= 3
            res |= (s << i)
        # handle negative numbers
        if res >= 2**31:
            res -= 2**32
        return res

    # Optimal best approach using ones and twos masks
    def singleNumberOptimal(self, nums: List[int]) -> int:
        ones = 0
        twos = 0
        for num in nums:
            ones = (ones ^ num) & (~twos)
            twos = (twos ^ num) & (~ones)
        return ones

    # Sorting approach
    def singleNumberSort(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        if nums[0] != nums[1]:
            return nums[0]
        if nums[-1] != nums[-2]:
            return nums[-1]
        i = 1
        while i < n:
            if nums[i] != nums[i-1]:
                return nums[i-1]
            i += 3
        return -1  # fallback (should not occur)

    # Set-sum formula approach
    def singleNumberSet(self, nums: List[int]) -> int:
        return (3 * sum(set(nums)) - sum(nums)) // 2


# -------- Driver Code --------
solution = Solution()

nums_list = [
    [2,2,3,2], 
    [0,1,0,1,0,1,99], 
    [-2,-2,1,-2], 
    [30000,500,100,30000,100,30000,100]
]

for nums in nums_list:
    print("Bitwise count:", solution.singleNumber(nums))
    print("Optimal ones/twos:", solution.singleNumberOptimal(nums))
    print("Sorting approach:", solution.singleNumberSort(nums))
    print("Set-sum formula:", solution.singleNumberSet(nums))
    print("-----")
