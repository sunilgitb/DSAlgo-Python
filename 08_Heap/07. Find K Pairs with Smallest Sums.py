import heapq
from typing import List

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        maxHeap = []

        for i in range(0, min(k, len(nums1))):
            for j in range(0, min(k, len(nums2))):
                x = nums1[i]
                y = nums2[j]
                total = x + y

                if len(maxHeap) < k:
                    heapq.heappush(maxHeap, [-total, x, y])
                else:
                    if total > -maxHeap[0][0]:
                        break
                    heapq.heappush(maxHeap, [-total, x, y])
                    heapq.heappop(maxHeap)

        result = []
        while maxHeap:
            popped = heapq.heappop(maxHeap)
            result.append([popped[1], popped[2]])

        return result


# ---------------- DRIVER CODE ----------------
if __name__ == "__main__":
    sol = Solution()

    nums1 = [1, 7, 11]
    nums2 = [2, 4, 6]
    k = 3
    print("K smallest pairs:", sol.kSmallestPairs(nums1, nums2, k))
    # Expected: [[1,2],[1,4],[1,6]] or in any order

    nums1 = [1, 1, 2]
    nums2 = [1, 2, 3]
    k = 2
    print("K smallest pairs:", sol.kSmallestPairs(nums1, nums2, k))
    # Expected: [[1,1],[1,1]]

    nums1 = [1, 2]
    nums2 = [3]
    k = 3
    print("K smallest pairs:", sol.kSmallestPairs(nums1, nums2, k))
    # Expected: [[1,3],[2,3]]
