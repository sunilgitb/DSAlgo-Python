# https://practice.geeksforgeeks.org/problems/k-th-element-of-two-sorted-array1317/1
# https://youtu.be/nv7F4PiLUzo

class Solution:
    def kthElement(self, nums1, nums2, n, m, k):
        # Always apply binary search on smaller array
        if n > m:
            return self.kthElement(nums2, nums1, m, n, k)

        low = max(0, k - m)
        high = min(k, n)

        INT_MIN = -10**18
        INT_MAX = 10**18

        while low <= high:
            cut1 = (low + high) // 2
            cut2 = k - cut1

            left1 = nums1[cut1 - 1] if cut1 > 0 else INT_MIN
            left2 = nums2[cut2 - 1] if cut2 > 0 else INT_MIN

            right1 = nums1[cut1] if cut1 < n else INT_MAX
            right2 = nums2[cut2] if cut2 < m else INT_MAX

            if left1 <= right2 and left2 <= right1:
                return max(left1, left2)
            elif left1 > right2:
                high = cut1 - 1
            else:
                low = cut1 + 1

        return -1


# ---------------- DRIVER CODE ----------------

sol = Solution()

nums1 = [2, 3, 6, 7, 9]
nums2 = [1, 4, 8, 10]
k = 5
print(sol.kthElement(nums1, nums2, len(nums1), len(nums2), k))
# Expected Output: 6


nums1 = [1, 2, 3]
nums2 = [4, 5, 6]
k = 4
print(sol.kthElement(nums1, nums2, len(nums1), len(nums2), k))
# Expected Output: 4


nums1 = [100, 112, 256, 349, 770]
nums2 = [72, 86, 113, 119, 265, 445, 892]
k = 7
print(sol.kthElement(nums1, nums2, len(nums1), len(nums2), k))
# Expected Output: 256
