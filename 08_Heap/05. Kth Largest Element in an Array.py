# ---------- Method 1: Min Heap ----------
import heapq

class SolutionHeap:
    def findKthLargest(self, nums, k):
        minHeap = []
        for num in nums:
            heapq.heappush(minHeap, num)
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        return minHeap[0]

# ---------- Method 2: Quick Select ----------
class SolutionQuick:
    def findKthLargest(self, nums, k):
        pivot = nums[0]
        left = [num for num in nums if num < pivot]
        equal = [num for num in nums if num == pivot]
        right = [num for num in nums if num > pivot]
        
        if k <= len(right):
            return self.findKthLargest(right, k)
        elif len(right) < k <= len(right) + len(equal):
            return equal[0]
        else:
            return self.findKthLargest(left, k - len(right) - len(equal))


# ---------------- DRIVER CODE ----------------
nums = [3,2,1,5,6,4]
k = 2

sol1 = SolutionHeap()
print("Method 1 (Heap) Output:", sol1.findKthLargest(nums, k))  # Output: 5

sol2 = SolutionQuick()
print("Method 2 (Quick Select) Output:", sol2.findKthLargest(nums, k))  # Output: 5
