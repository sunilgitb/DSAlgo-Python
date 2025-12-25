# https://practice.geeksforgeeks.org/problems/the-painters-partition-problem1535/1/#

# SAME AS MINIMUM NUMBER OF PAGE ALLOCATION PROBLEM using Binary Search

class Solution:
    def minTime (self, arr, n, k):
        
        def isValid(mid):
            count = 1
            s = 0
            for i in arr:
                s += i
                if s > mid:
                    count += 1
                    s = i
            return count <= k
        
        low = min(arr)
        high = sum(arr)
        while low <= high:
            mid = low + (high - low) // 2
            if isValid(mid):
                high = mid - 1
            else:
                low = mid + 1
        
        return low

# the sum(arr) can at max 2^32 so max high = 2^32 
# Time: O(log(2^32) * n) = 32 * n  
# Space: O(1)


if __name__ == "__main__":
    # ✅ Driver code with example tests
    s = Solution()

    tests = [
        ([10, 10, 10, 10], 2, 20),       # split into [10,10] and [10,10]
        ([10, 20, 30, 40], 2, 60),       # best split [10,20,30] | [40]
        ([10, 20, 30, 40, 50], 3, 60),   # best split [10,20,30] | [40] | [50]
        ([1, 1, 1, 1, 1], 2, 3),         # split 3 and 2
        ([7, 5, 5], 3, 7),               # k >= n -> max element
        ([5, 5, 5], 1, 15),              # single painter -> sum
    ]

    for i, (arr, k, expected) in enumerate(tests, 1):
        res = s.minTime(arr, len(arr), k)
        print(f"Test {i}: arr={arr}, k={k} -> minTime={res} (expected={expected})")

