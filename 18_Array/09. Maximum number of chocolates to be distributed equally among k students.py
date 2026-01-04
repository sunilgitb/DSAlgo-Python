# https://www.geeksforgeeks.org/maximum-number-chocolates-distributed-equally-among-k-students/

"""
Approach:
- We need the maximum sum of a subarray such that (sum % k == 0)
- Use prefix sum + hashmap to store first occurrence of remainder
- If two prefix sums have the same remainder, their difference is divisible by k
"""

def maxNumOfChocolates(arr, k):
    prefix_sum = 0
    remainder_sum = {}   # remainder -> first prefix_sum
    max_sum = 0

    for num in arr:
        prefix_sum += num
        rem = prefix_sum % k

        # Case 1: whole prefix divisible by k
        if rem == 0:
            max_sum = max(max_sum, prefix_sum)

        # Case 2: first time this remainder appears
        elif rem not in remainder_sum:
            remainder_sum[rem] = prefix_sum

        # Case 3: remainder seen before
        else:
            max_sum = max(max_sum, prefix_sum - remainder_sum[rem])

    return max_sum // k



# ---------------- DRIVER CODE ----------------
if __name__ == "__main__":
    arr = [2, 7, 6, 1, 4, 5]
    k = 3

    print("Maximum number of chocolates:",
          maxNumOfChocolates(arr, k))
