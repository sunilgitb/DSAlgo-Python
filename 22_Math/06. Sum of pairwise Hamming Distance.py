# https://www.interviewbit.com/problems/sum-of-pairwise-hamming-distance/ 

"""
File: Sum of Pairwise Hamming Distance.py

Problem:
Given an array of integers A, find the sum of pairwise Hamming distances.
Hamming distance between two integers is the number of differing bits.

InterviewBit:
https://www.interviewbit.com/problems/sum-of-pairwise-hamming-distance/
"""

MOD = 1000000007

# ------------------------------------------------------------
# Solution Class
# ------------------------------------------------------------

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def hammingDistance(self, A):
        res = 0

        # Check each bit position (0 to 31)
        for i in range(32):
            n0 = n1 = 0

            for a in A:
                if a & (1 << i):
                    n1 += 1
                else:
                    n0 += 1

            # Each differing pair contributes twice
            res += 2 * n0 * n1

        return res % MOD


# ------------------------------------------------------------
# Driver Code
# ------------------------------------------------------------
if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        (1, 3, 5),
        (2, 4, 6),
        (1, 1, 1),
        (0, 0),
        (4, 14, 2)
    ]

    for A in test_cases:
        print(f"Array: {A}")
        print("Sum of Pairwise Hamming Distance:", sol.hammingDistance(A))
        print("-" * 50)


"""
Output:
Array: (1, 3, 5)
Sum of Pairwise Hamming Distance: 8
--------------------------------------------------
Array: (2, 4, 6)
Sum of Pairwise Hamming Distance: 8
--------------------------------------------------
Array: (1, 1, 1)
Sum of Pairwise Hamming Distance: 0
--------------------------------------------------
Array: (0, 0)
Sum of Pairwise Hamming Distance: 0
--------------------------------------------------
Array: (4, 14, 2)
Sum of Pairwise Hamming Distance: 12
--------------------------------------------------
"""

# ------------------------------------------------------------
# Time Complexity: O(32 * N) ≈ O(N)
# Space Complexity: O(1)
# ------------------------------------------------------------
