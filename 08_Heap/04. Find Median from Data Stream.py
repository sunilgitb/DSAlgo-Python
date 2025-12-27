import heapq

class MedianFinder:

    def __init__(self):
        self.small = []   # Max Heap (store negative values)
        self.large = []   # Min Heap

    def addNum(self, num: int) -> None:
        # Step 1: Always push to max heap
        heapq.heappush(self.small, -num)

        # Step 2: Order property
        if self.small and self.large and -self.small[0] > self.large[0]:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        # Step 3: Balance heaps
        if len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]

        if len(self.large) > len(self.small):
            return self.large[0]

        return (-self.small[0] + self.large[0]) / 2


# ---------------- DRIVER CODE ----------------
mf = MedianFinder()

mf.addNum(1)
print(mf.findMedian())   # Output: 1

mf.addNum(2)
print(mf.findMedian())   # Output: 1.5

mf.addNum(3)
print(mf.findMedian())   # Output: 2

mf.addNum(4)
print(mf.findMedian())   # Output: 2.5
