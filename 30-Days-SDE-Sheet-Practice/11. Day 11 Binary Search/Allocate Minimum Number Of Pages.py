# https://practice.geeksforgeeks.org/problems/allocate-minimum-number-of-pages0937
# https://www.youtube.com/watch?v=2JSQIhPcHQg

'''
Allocate Minimum Number of Pages (Binary Search on Answer)

Each student must get contiguous books.
We want to minimize the maximum pages assigned to any student.
'''

class Solution:
    def findPages(self, A, N, M):

        # If books are fewer than students
        if N < M:
            return -1

        l = max(A)     # minimum possible answer
        r = sum(A)     # maximum possible answer
        ans = -1

        def isValid(mid):
            pageSum = 0
            students = 1

            for pages in A:
                pageSum += pages
                if pageSum > mid:
                    students += 1
                    pageSum = pages
                if students > M:
                    return False
            return True

        while l <= r:
            mid = l + (r - l) // 2
            if isValid(mid):
                ans = mid
                r = mid - 1
            else:
                l = mid + 1

        return ans


# -------- DRIVER CODE --------

sol = Solution()

print(sol.findPages([12, 34, 67, 90], 4, 2))
# Expected Output: 113

print(sol.findPages([10, 20, 30, 40], 4, 2))
# Expected Output: 60

print(sol.findPages([5, 17, 100, 11], 4, 4))
# Expected Output: 100

print(sol.findPages([15, 10, 19, 10, 5], 5, 2))
# Expected Output: 34
