# https://practice.geeksforgeeks.org/problems/subset-sums2234/1#

'''
Make the recursion TREE of the problem. one chile including the current element
and other child Not including the current element
'''
# Problem: https://practice.geeksforgeeks.org/problems/subset-sums2234/1
# Subset Sums - Print all possible subset sums of the given array

class Solution:
    def subsetSums(self, arr, N):
        res = []
        
        def solve(i, current_sum):
            # Base case: we've considered all elements
            if i == len(arr):
                res.append(current_sum)
                return
            
            # Two choices (two children in recursion tree):
            # 1. Include the current element
            solve(i + 1, current_sum + arr[i])
            
            # 2. Exclude the current element
            solve(i + 1, current_sum)
        
        # Start recursion from index 0 with sum 0
        solve(0, 0)
        return res


# ──────────────────────────────────────────────────────────────
# Driver Code (for local testing)
# ──────────────────────────────────────────────────────────────

if __name__ == "__main__":
    # Test Case 1
    arr1 = [2, 3]
    N1 = len(arr1)
    sol = Solution()
    result1 = sol.subsetSums(arr1, N1)
    print("Input:", arr1)
    print("Subset sums:", sorted(result1))  # Sorted for readability
    # Expected: [0, 2, 3, 5]

    print("-" * 50)

    # Test Case 2
    arr2 = [1, 2, 3]
    N2 = len(arr2)
    result2 = sol.subsetSums(arr2, N2)
    print("Input:", arr2)
    print("Subset sums:", sorted(result2))
    # Expected: [0, 1, 2, 3, 1+2=3, 1+3=4, 2+3=5, 1+2+3=6]

    print("-" * 50)

    # Test Case 3 (single element)
    arr3 = [5]
    result3 = sol.subsetSums(arr3, len(arr3))
    print("Input:", arr3)
    print("Subset sums:", sorted(result3))
    # Expected: [0, 5]
# Time: O(2 ^ N)  # as for each element we are calling 2 different calls
# Space: O(N)