# https://leetcode.com/problems/online-stock-span/

class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        span = 1
        leftmost = 0
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack.pop()[1]
        
        self.stack.append((price, span))
        return span

# Example Usage:
stockSpanner = StockSpanner()
print(stockSpanner.next(100))  # return 1
print(stockSpanner.next(80))   # return 1
print(stockSpanner.next(60))   # return 1
print(stockSpanner.next(70))   # return 2

# Time: O(N)
# Space: O(N)
