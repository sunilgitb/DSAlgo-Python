# https://practice.geeksforgeeks.org/problems/subset-sums2234/1#

'''
Make the recursion TREE of the problem. one chile including the current element
and other child Not including the current element
'''
# https://practice.geeksforgeeks.org/problems/subset-sums2234/1#

'''
Make the recursion TREE of the problem.
One child includes the current element,
another child does NOT include the current element.
'''

class Solution:
    def subsetSums(self, arr, N):
        res = []

        def solve(i, s):
            if i == N:
                res.append(s)
                return

            # Include current element
            solve(i + 1, s + arr[i])

            # Exclude current element
            solve(i + 1, s)

        solve(0, 0)
        return res


# -------- DRIVER CODE --------
sol = Solution()

arr = [1, 2, 3]
N = len(arr)

print(sol.subsetSums(arr, N))
# Expected Output: [6, 3, 4, 1, 5, 2, 3, 0]

arr = [5, 2]
N = len(arr)

print(sol.subsetSums(arr, N))
# Expected Output: [7, 5, 2, 0]

arr = [0]
N = len(arr)

print(sol.subsetSums(arr, N))
# Expected Output: [0, 0]

		
# Time: O(2 ^ N)  # as for each element we are calling 2 different calls
# Space: O(N)