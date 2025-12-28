# 09. Design a Stack that supports getMin() in O(1) time and O(1) extra space
# Problem: Implement a stack with push, pop, top, and getMin operations,
# where getMin() returns the minimum element in the stack in constant time.
# Extra space should be O(1) (not O(n)).

# Approach: Use a single stack and store (value, current_min) pairs
# - When pushing a new value:
#   - If value >= current_min → push (value, current_min)
#   - If value < current_min    → push (value, value) and update current_min
# - When popping:
#   - Pop the top pair, and update current_min to the new top's min (if stack not empty)

class MinStack:
    def __init__(self):
        """
        Initialize the stack as empty.
        We use a list of tuples: (value, min_so_far)
        """
        self.stack = []  # list of (value, min_at_that_time)

    def push(self, val: int) -> None:
        """
        Push a value onto the stack.
        O(1) time.
        """
        if not self.stack:
            # First element: min is itself
            self.stack.append((val, val))
        else:
            current_min = self.stack[-1][1]
            new_min = min(current_min, val)
            self.stack.append((val, new_min))

    def pop(self) -> None:
        """
        Remove the top element from the stack.
        O(1) time.
        """
        if self.stack:
            self.stack.pop()

    def top(self) -> int:
        """
        Get the top element.
        O(1) time.
        """
        if not self.stack:
            raise IndexError("Stack is empty")
        return self.stack[-1][0]

    def getMin(self) -> int:
        """
        Get the minimum element in the stack.
        O(1) time.
        """
        if not self.stack:
            raise IndexError("Stack is empty")
        return self.stack[-1][1]


# Driver Code with multiple test cases
def run_tests():
    test_cases = [
        # Test 1: Standard usage
        (["MinStack", "push", "push", "push", "getMin", "pop", "top", "getMin"],
         [[], [-2], [0], [-3], [], [], [], []],
         [None, None, None, None, -3, None, 0, -2]),

        # Test 2: All decreasing
        (["MinStack", "push", "push", "push", "getMin", "pop", "getMin"],
         [[], [5], [4], [3], [], [], []],
         [None, None, None, None, 3, None, 4]),

        # Test 3: Duplicates
        (["MinStack", "push", "push", "push", "getMin", "pop", "getMin"],
         [[], [1], [1], [1], [], [], []],
         [None, None, None, None, 1, None, 1]),

        # Test 4: Single element
        (["MinStack", "push", "getMin", "pop", "getMin"],
         [[], [10], [], [], []],
         [None, None, 10, None, "Error"]),

        # Test 5: Empty stack operations
        (["MinStack", "getMin", "pop"],
         [[], [], []],
         [None, "Error", "Error"]),
    ]

    print("Testing Min Stack with O(1) getMin()\n" + "="*50)

    for idx, (operations, args, expected) in enumerate(test_cases, 1):
        print(f"\nTest {idx}:")
        min_stack = MinStack()
        results = []

        for op, arg in zip(operations, args):
            try:
                if op == "MinStack":
                    min_stack = MinStack()
                    results.append(None)
                elif op == "push":
                    min_stack.push(arg[0])
                    results.append(None)
                elif op == "pop":
                    min_stack.pop()
                    results.append(None)
                elif op == "top":
                    results.append(min_stack.top())
                elif op == "getMin":
                    results.append(min_stack.getMin())
            except IndexError:
                results.append("Error")

        status = "✓ PASS" if results == expected else "✗ FAIL"
        print(f"   Operations: {operations}")
        print(f"   Args:       {args}")
        print(f"   Output:     {results}")
        print(f"   Expected:   {expected}")
        print(f"   Status:     {status}")


if __name__ == "__main__":
    run_tests()