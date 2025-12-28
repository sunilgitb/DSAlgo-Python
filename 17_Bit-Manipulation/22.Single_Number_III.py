# https://leetcode.com/problems/single-number-iii/
# https://www.youtube.com/watch?v=faoVORjd-T8

class Solution:
    def singleNumber(self, nums: list[int]) -> list[int]:
        xor = 0
        for num in nums:
            xor ^= num
        
        # Find a bit that is different between the two unique numbers
        diff_bit = 1
        while not (xor & diff_bit):
            diff_bit <<= 1
        
        xorGroupA = xorGroupB = 0
        for num in nums:
            if num & diff_bit:
                xorGroupA ^= num
            else:
                xorGroupB ^= num
        
        return [xorGroupA, xorGroupB]

# ---------------- Driver Code ----------------
solution = Solution()

print(solution.singleNumber([1,2,1,3,2,5]))  # Expected output: [3,5] or [5,3]
print(solution.singleNumber([-1,0]))         # Expected output: [-1,0] or [0,-1]
print(solution.singleNumber([2,1,2,3]))      # Expected output: [1,3] or [3,1]
