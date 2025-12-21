# https://practice.geeksforgeeks.org/problems/largest-subarray-with-0-sum/1#
'''
Use a dictionary to store current sum if we get same sum later then it must be zero in that range.
'''

# https://practice.geeksforgeeks.org/problems/largest-subarray-with-0-sum/1#
'''
Use a dictionary to store prefix sum.
If the same sum appears again, the subarray in between has sum = 0.
'''

class Solution:
    def maxLen(self, n, arr):
        prefix_index = {0: -1}   # sum : first index
        s = 0
        res = 0

        for i in range(n):
            s += arr[i]

            if s in prefix_index:
                res = max(res, i - prefix_index[s])
            else:
                prefix_index[s] = i

        return res


# ---------------- DRIVER CODE ----------------
if __name__ == "__main__":
    sol = Solution()

    arr = [15, -2, 2, -8, 1, 7, 10, 23]
    n = len(arr)

    print("Array:", arr)
    print("Length of largest subarray with 0 sum:", sol.maxLen(n, arr))


# Time: O(n)
# Space: O(n)