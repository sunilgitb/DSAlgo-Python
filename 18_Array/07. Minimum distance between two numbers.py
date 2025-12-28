# https://practice.geeksforgeeks.org/problems/minimum-distance-between-two-numbers/1

'''
class Solution:
    def minDist(self, arr, n, x, y):
        res = 2**31
        j = 0
        for i in range(n):
            while arr[i] == x and j < i:
                if arr[j] == y: res = min(res, i - j)
                j += 1
        j = 0
        for i in range(n):
            while arr[i] == y and j < i:
                if arr[j] == x: res = min(res, i - j)
                j += 1

        return res if res != 2**31 else -1
'''

class Solution:
    def minDist(self, arr, n, x, y):
        res = 2**31
        ix = iy = -1
        
        for i in range(n):
            if arr[i] == x:
                ix = i
            if arr[i] == y:
                iy = i
            if ix != -1 and iy != -1:
                res = min(res, abs(ix - iy))
        
        return res if res != 2**31 else -1


# ---------------- DRIVER CODE ----------------
if __name__ == "__main__":
    solution = Solution()

    arr = [1, 2, 3, 2]
    n = len(arr)
    x, y = 1, 2
    print(solution.minDist(arr, n, x, y))   # Output: 1

    arr = [86, 39, 90, 67, 84, 66, 62]
    n = len(arr)
    x, y = 42, 12
    print(solution.minDist(arr, n, x, y))   # Output: -1

    arr = [3, 5, 4, 2, 6, 5, 6, 6, 5, 4, 8, 3]
    n = len(arr)
    x, y = 3, 6
    print(solution.minDist(arr, n, x, y))   # Output: 4

      
'''
Time Complexity: O(N)
Auxiliary Space: O(1)
'''
