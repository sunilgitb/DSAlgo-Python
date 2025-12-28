# https://leetcode.com/problems/hamming-distance/
# https://www.geeksforgeeks.org/hamming-distance-between-two-integers/

'''
The Hamming distance between two integers is the number of positions
at which the corresponding bits are different.

Example: Hamming distance between 4 (0100) and 14 (1110) is 2.
Two bits differ at corresponding positions.
'''

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        res = 0
        for i in range(32):
            if (x & (1 << i)) != (y & (1 << i)):
                res += 1
        return res

# -------- Driver Code --------
solution = Solution()

print(solution.hammingDistance(4, 14))   # 2
print(solution.hammingDistance(1, 4))    # 2
print(solution.hammingDistance(0, 0))    # 0
print(solution.hammingDistance(25, 30))  # 4
