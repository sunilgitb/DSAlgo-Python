# https://practice.geeksforgeeks.org/problems/find-nth-root-of-m5843/1/

# https://youtu.be/WjpswYrS2nY

class Solution:
    def NthRoot(self, n, num):
        r = num
        l = 1

        while l <= r:
            mid = (l + r) // 2
            if mid ** n < num:
                l = mid + 1
            elif mid ** n > num:
                r = mid - 1
            else:
                return mid

        return -1

# Time: O(log(num))
# Space: O(1)


if __name__ == "__main__":
    # ✅ Driver code with example tests
    s = Solution()

    tests = [
        (2, 16, 4),      # 2nd root of 16 is 4
        (3, 27, 3),      # 3rd root of 27 is 3
        (5, 32, 2),      # 5th root of 32 is 2
        (4, 15, -1),     # no integer 4th root
        (1, 7, 7),       # 1st root of n is n
    ]

    for i, (n, num, expected) in enumerate(tests, 1):
        res = s.NthRoot(n, num)
        print(f"Test {i}: n={n}, num={num} -> root={res} (expected={expected})")