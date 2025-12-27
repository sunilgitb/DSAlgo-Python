# Method 1: Doubly Linked List
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        self.prev = None

class BrowserHistory_DLL:
    def __init__(self, homepage: str):
        self.head = ListNode(homepage)

    def visit(self, url: str) -> None:
        node = ListNode(url)
        node.prev = self.head
        self.head.next = node
        self.head = node

    def back(self, steps: int) -> str:
        while steps and self.head.prev:
            self.head = self.head.prev
            steps -= 1
        return self.head.val

    def forward(self, steps: int) -> str:
        while steps and self.head.next:
            self.head = self.head.next
            steps -= 1
        return self.head.val


# Method 2: Array
class BrowserHistory_Array:
    def __init__(self, homepage: str):
        self.pages = [homepage]
        self.i = 0

    def visit(self, url: str) -> None:
        self.pages = self.pages[:self.i+1] + [url]
        self.i += 1

    def back(self, steps: int) -> str:
        self.i = max(0, self.i - steps)
        return self.pages[self.i]
        
    def forward(self, steps: int) -> str:
        self.i = min(len(self.pages) - 1, self.i + steps)
        return self.pages[self.i]


# Test both implementations
print("Testing Browser History:")
print("=" * 80)

# Test Case 1: Basic operations
operations = ["BrowserHistory", "visit", "visit", "visit", "back", "back", "forward", "visit", "forward", "back", "back"]
values = [["leetcode.com"], ["google.com"], ["facebook.com"], ["youtube.com"], [1], [1], [1], ["linkedin.com"], [2], [2], [7]]
expected = [None, None, None, None, "facebook.com", "google.com", "facebook.com", None, "linkedin.com", "google.com", "leetcode.com"]

print("Test Case 1: Basic operations")
print("-" * 80)

# Test Doubly Linked List implementation
print("Doubly Linked List Implementation:")
dll_browser = BrowserHistory_DLL(values[0][0])
results_dll = [None]

for op, val in zip(operations[1:], values[1:]):
    if op == "visit":
        dll_browser.visit(val[0])
        results_dll.append(None)
    elif op == "back":
        result = dll_browser.back(val[0])
        results_dll.append(result)
        print(f"  back({val[0]}) -> {result}")
    elif op == "forward":
        result = dll_browser.forward(val[0])
        results_dll.append(result)
        print(f"  forward({val[0]}) -> {result}")

print()

# Test Array implementation
print("Array Implementation:")
array_browser = BrowserHistory_Array(values[0][0])
results_array = [None]

for op, val in zip(operations[1:], values[1:]):
    if op == "visit":
        array_browser.visit(val[0])
        results_array.append(None)
    elif op == "back":
        result = array_browser.back(val[0])
        results_array.append(result)
        print(f"  back({val[0]}) -> {result}")
    elif op == "forward":
        result = array_browser.forward(val[0])
        results_array.append(result)
        print(f"  forward({val[0]}) -> {result}")

print()

# Compare results
print("Comparison:")
print(f"Expected results:    {expected}")
print(f"DLL results:         {results_dll}")
print(f"Array results:       {results_array}")

dll_match = all(r == e for r, e in zip(results_dll, expected))
array_match = all(r == e for r, e in zip(results_array, expected))

print(f"\nDLL implementation matches expected: {'✓' if dll_match else '✗'}")
print(f"Array implementation matches expected: {'✓' if array_match else '✗'}")

print("\n" + "=" * 80)
print("\nTest Case 2: Edge cases")

# Test edge cases
edge_browser_dll = BrowserHistory_DLL("home.com")
edge_browser_array = BrowserHistory_Array("home.com")

print("\n1. Back beyond history:")
print(f"   DLL: back(10) -> {edge_browser_dll.back(10)} (should be 'home.com')")
print(f"   Array: back(10) -> {edge_browser_array.back(10)} (should be 'home.com')")

print("\n2. Forward beyond history:")
print(f"   DLL: forward(10) -> {edge_browser_dll.forward(10)} (should be 'home.com')")
print(f"   Array: forward(10) -> {edge_browser_array.forward(10)} (should be 'home.com')")

print("\n3. Visit after going back (should clear forward history):")
edge_browser_dll.visit("page1.com")
edge_browser_dll.visit("page2.com")
edge_browser_dll.back(1)  # Go to page1.com

edge_browser_array.visit("page1.com")
edge_browser_array.visit("page2.com")
edge_browser_array.back(1)  # Go to page1.com

print(f"   Current DLL position: {edge_browser_dll.head.val} (should be 'page1.com')")
print(f"   Current Array position: {edge_browser_array.pages[edge_browser_array.i]} (should be 'page1.com')")

edge_browser_dll.visit("page3.com")
edge_browser_array.visit("page3.com")

print(f"   After visiting page3.com:")
print(f"   DLL forward(1) -> {edge_browser_dll.forward(1)} (should be 'page3.com')")
print(f"   Array forward(1) -> {edge_browser_array.forward(1)} (should be 'page3.com')")