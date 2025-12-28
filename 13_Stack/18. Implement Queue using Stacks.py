# https://leetcode.com/problems/implement-queue-using-stacks/

class MyQueue:

    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:     # O(1)
        self.stack = [x] + self.stack
        
    def pop(self) -> int:               # O(1)
        return self.stack.pop()

    def peek(self) -> int:              # O(1)
        return self.stack[-1]

    def empty(self) -> bool:            # O(1)
        return len(self.stack) == 0


# Driver Code:
obj = MyQueue()
obj.push(1)
obj.push(2)
print(obj.peek())  # returns 1
print(obj.pop())   # returns 1
print(obj.empty()) # returns False  
