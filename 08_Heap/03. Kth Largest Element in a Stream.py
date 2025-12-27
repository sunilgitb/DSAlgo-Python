import heapq
from typing import List

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.minHeap = []

        for num in nums:
            heapq.heappush(self.minHeap, num)

        # keep only k largest elements
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]


# ---------------- DRIVER CODE ----------------
k = 3
nums = [4, 5, 8, 2]
obj = KthLargest(k, nums)

print(obj.add(3))   # Output: 4
print(obj.add(5))   # Output: 5
print(obj.add(10))  # Output: 5
print(obj.add(9))   # Output: 8
print(obj.add(4))   # Output: 8

import heapq
from typing import List

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = []
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]


# ---------------- DRIVER CODE ----------------
k = 3
nums = [4, 5, 8, 2]
obj = KthLargest(k, nums)

print(obj.add(3))   # Output: 4
print(obj.add(5))   # Output: 5
print(obj.add(10))  # Output: 5
print(obj.add(9))   # Output: 8
print(obj.add(4))   # Output: 8
