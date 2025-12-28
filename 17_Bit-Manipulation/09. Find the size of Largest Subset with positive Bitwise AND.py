# https://www.geeksforgeeks.org/find-the-size-of-largest-subset-with-positive-bitwise-and/

# Python 3 program for the above approach

# Function to find the largest possible
# subset having Bitwise AND positive
# https://www.geeksforgeeks.org/find-the-size-of-largest-subset-with-positive-bitwise-and/

from typing import List

class Solution:
    def largestSubset(self, arr: List[int]) -> int:
        # Stores the number of set bits at each bit position (0-31)
        bit = [0] * 32

        # Traverse the array
        for num in arr:
            x = 31  # Start from the most significant bit
            n = num
            while n > 0:
                if n & 1:  # Last bit is set
                    bit[x] += 1
                n = n >> 1
                x -= 1

        # Size of largest subset with positive AND
        return max(bit)


# -------- Driver Code --------
solution = Solution()

arr_list = [
    [7, 13, 8, 2, 3],    # Example from GFG
    [1, 2, 4, 8, 16],    # Powers of 2
    [3, 3, 3, 3],        # All same
    [5, 7, 15, 3, 1]     # Mixed numbers
]

for arr in arr_list:
    print("Array:", arr)
    print("Largest subset size with positive AND:", solution.largestSubset(arr))
    print("-----")


	# This code is contributed by ipg016107.

