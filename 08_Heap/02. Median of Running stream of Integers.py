import heapq

class Solution:
    def __init__(self):
        self.min_heap = []  # larger half
        self.max_heap = []  # smaller half (negative values)

    def insertHeaps(self, x):
        heapq.heappush(self.max_heap, -x)
        heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        if len(self.min_heap) > len(self.max_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

    def getMedian(self):
        if len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        return (-self.max_heap[0] + self.min_heap[0]) // 2


# -------- DRIVER CODE --------
stream = [5, 15, 1, 3]
obj = Solution()

for num in stream:
    obj.insertHeaps(num)
    print(obj.getMedian(), end=" ")
