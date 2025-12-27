import heapq

class MedianFinder:

    def __init__(self):
        self.small = []   # Max Heap (store negative values)
        self.large = []   # Min Heap

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -num)
        
        if self.small and self.large and -self.small[0] > self.large[0]:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        
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


# Test the MedianFinder
operations = ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian"]
values = [[], [1], [2], [], [3], [], [4], [], [5], [], [6], []]

print("Testing Median Finder:")
print("-" * 50)

mf = None
results = []

for op, val in zip(operations, values):
    if op == "MedianFinder":
        mf = MedianFinder()
        results.append(None)
    elif op == "addNum":
        mf.addNum(val[0])
        results.append(None)
    elif op == "findMedian":
        median = mf.findMedian()
        results.append(median)
        print(f"After operations: Median = {median}")

print("\nComplete operations:")
for op, val, res in zip(operations, values, results):
    if op == "addNum":
        print(f"{op}({val[0]}) -> {res}")
    elif op == "findMedian":
        print(f"{op}() -> {res}")
    else:
        print(f"{op}() -> {res}")