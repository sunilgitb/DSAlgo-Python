class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}  # map key to node
        
        # Dummy nodes to mark boundaries
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    # Remove node from list
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev
    
    # Insert node at right (most recently used)
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev
        
    def get(self, key: int) -> int:
        if key in self.cache:
            # Move to most recently used
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Update existing key
            self.remove(self.cache[key])
        
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
        
        if len(self.cache) > self.cap:
            # Remove least recently used
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

    def print_cache(self):
        """Helper method to print cache state"""
        result = []
        current = self.left.next
        while current != self.right:
            result.append(f"({current.key}:{current.val})")
            current = current.next
        print(f"Cache: {' -> '.join(result)}")
        print(f"Cache keys: {list(self.cache.keys())}")


# Test the LRU Cache
print("Testing LRU Cache:")
print("=" * 80)

lru = LRUCache(2)
print("Initialized LRU Cache with capacity 2")

print("\n1. Put (1, 1):")
lru.put(1, 1)
lru.print_cache()

print("\n2. Put (2, 2):")
lru.put(2, 2)
lru.print_cache()

print("\n3. Get key 1:")
print(f"   Result: {lru.get(1)} (expected: 1)")
lru.print_cache()

print("\n4. Put (3, 3): (This should evict key 2)")
lru.put(3, 3)
lru.print_cache()

print("\n5. Get key 2:")
print(f"   Result: {lru.get(2)} (expected: -1)")
lru.print_cache()

print("\n6. Get key 3:")
print(f"   Result: {lru.get(3)} (expected: 3)")
lru.print_cache()

print("\n7. Get key 1:")
print(f"   Result: {lru.get(1)} (expected: 1)")
lru.print_cache()

print("\n8. Put (4, 4): (This should evict key 3)")
lru.put(4, 4)
lru.print_cache()

print("\n9. Get key 3:")
print(f"   Result: {lru.get(3)} (expected: -1)")
lru.print_cache()

print("\n10. Get key 4:")
print(f"    Result: {lru.get(4)} (expected: 4)")
lru.print_cache()

print("\n11. Get key 1:")
print(f"    Result: {lru.get(1)} (expected: 1)")
lru.print_cache()

print("\n" + "=" * 80)
print("\nAdditional test cases:")

# Test case 2: Capacity 1
print("\nTesting LRU Cache with capacity 1:")
lru2 = LRUCache(1)
lru2.put(2, 1)
print(f"After put(2, 1): get(2) = {lru2.get(2)} (expected: 1)")
lru2.put(3, 2)
print(f"After put(3, 2): get(2) = {lru2.get(2)} (expected: -1)")
print(f"After put(3, 2): get(3) = {lru2.get(3)} (expected: 2)")

# Test case 3: Update existing key
print("\nTesting update existing key:")
lru3 = LRUCache(2)
lru3.put(1, 1)
lru3.put(2, 2)
lru3.put(1, 10)  # Update key 1
print(f"After updating key 1 to 10: get(1) = {lru3.get(1)} (expected: 10)")
print(f"get(2) = {lru3.get(2)} (expected: 2)")

# Test case 4: Complex sequence
print("\nTesting complex sequence:")
lru4 = LRUCache(3)
operations = [
    ("put", 1, 1),
    ("put", 2, 2),
    ("put", 3, 3),
    ("put", 4, 4),  # Should evict 1
    ("get", 1, -1),  # Should return -1
    ("get", 2, 2),   # Should return 2
    ("put", 5, 5),   # Should evict 3
    ("get", 3, -1),  # Should return -1
    ("get", 4, 4),   # Should return 4
    ("get", 5, 5),   # Should return 5
]

print("\nOperations:")
for op, key, expected in operations:
    if op == "put":
        lru4.put(key, expected)
        print(f"  put({key}, {expected})")
    else:
        result = lru4.get(key)
        status = "✓" if result == expected else "✗"
        print(f"  get({key}) = {result} (expected: {expected}) {status}")
    lru4.print_cache()