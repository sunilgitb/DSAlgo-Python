# https://leetcode.com/problems/implement-stack-using-queues/

# https://leetcode.com/problems/implement-stack-using-queues/
# Implement a stack using only a single queue.
# All operations should be O(1) amortized time.

from collections import deque

class MyStack:
    def __init__(self):
        self.q = deque()  # single queue

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        We append x, then rotate the queue so that x is at the front.
        Time: O(n)
        """
        self.q.append(x)
        # Rotate: move all previous elements to the back
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns it.
        Since we keep the top at the front, just popleft().
        Time: O(1)
        """
        return self.q.popleft()

    def top(self) -> int:
        """
        Get the top element.
        Returns the front of the queue.
        Time: O(1)
        """
        return self.q[0]

    def empty(self) -> bool:
        """
        Returns true if the stack is empty.
        Time: O(1)
        """
        return len(self.q) == 0


# Driver code to test the implementation
if __name__ == "__main__":
    print("Testing MyStack implementation\n" + "="*40)
    
    stack = MyStack()
    
    operations = [
        ("push", 1),
        ("push", 2),
        ("top", None),
        ("pop", None),
        ("top", None),
        ("empty", None),
        ("push", 3),
        ("top", None),
        ("empty", None),
    ]
    
    expected = [None, None, 2, 2, 1, False, None, 3, False]
    
    results = []
    for op, arg in operations:
        if op == "push":
            stack.push(arg)
            results.append(None)
        elif op == "pop":
            results.append(stack.pop())
        elif op == "top":
            results.append(stack.top())
        elif op == "empty":
            results.append(stack.empty())
    
    print("Operations:", [op for op, _ in operations])
    print("Results:   ", results)
    print("Expected:  ", expected)
    print("Status:    ", "✓ PASS" if results == expected else "✗ FAIL")