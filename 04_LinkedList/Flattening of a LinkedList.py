class Node:
    def __init__(self, d):
        self.data = d
        self.next = None
        self.bottom = None

def flatten(root):
    if not root or not root.next:
        return root
    
    # Merge two lists - root and root.next
    if root.data <= root.next.data:
        a = root
        b = root.next
        c = b.next
        head = a
    else:
        a = root.next
        b = root
        c = a.next
        head = a
    
    while a:
        if b and a.bottom and a.bottom.data > b.data:
            temp = a.bottom
            a.bottom = b
            b = temp
        elif not a.bottom:
            a.bottom = b
            b = None
        elif not a.bottom and not b:
            a.bottom = c
            break
        a = a.bottom
    
    head.next = c
    return flatten(head)

def print_flattened_list(head):
    """Print the flattened list using bottom pointers"""
    result = []
    current = head
    while current:
        result.append(str(current.data))
        current = current.bottom
    print(" -> ".join(result))

# Test case
def create_test_list():
    """
    Creates the test list from the problem statement:
    
    5 -> 10 -> 19 -> 28
    |     |     |     | 
    7     20    22   35
    |           |     | 
    8          50    40
    |                 | 
    30               45
    """
    
    # Create main nodes
    node5 = Node(5)
    node10 = Node(10)
    node19 = Node(19)
    node28 = Node(28)
    
    # Connect main nodes
    node5.next = node10
    node10.next = node19
    node19.next = node28
    
    # Create bottom nodes for node5
    node7 = Node(7)
    node8 = Node(8)
    node30 = Node(30)
    node5.bottom = node7
    node7.bottom = node8
    node8.bottom = node30
    
    # Create bottom nodes for node10
    node20 = Node(20)
    node10.bottom = node20
    
    # Create bottom nodes for node19
    node22 = Node(22)
    node50 = Node(50)
    node19.bottom = node22
    node22.bottom = node50
    
    # Create bottom nodes for node28
    node35 = Node(35)
    node40 = Node(40)
    node45 = Node(45)
    node28.bottom = node35
    node35.bottom = node40
    node40.bottom = node45
    
    return node5

print("Testing Flattening a Linked List:")
print("=" * 80)

print("\nOriginal list structure:")
print("5 -> 10 -> 19 -> 28")
print("|     |     |     |")
print("7     20    22   35")
print("|           |     |")
print("8          50    40")
print("|                 |")
print("30               45")

root = create_test_list()
flattened = flatten(root)

print("\nFlattened list (using bottom pointers):")
print_flattened_list(flattened)
print("Expected: 5 -> 7 -> 8 -> 10 -> 19 -> 20 -> 22 -> 28 -> 30 -> 35 -> 40 -> 45 -> 50")

print("\n" + "=" * 80)

# Additional test case
print("\nAdditional test case - Single list:")

# Create a single vertical list
node1 = Node(1)
node3 = Node(3)
node5 = Node(5)
node1.bottom = node3
node3.bottom = node5

flattened_single = flatten(node1)
print("Flattened single list:")
print_flattened_list(flattened_single)
print("Expected: 1 -> 3 -> 5")

print("\n" + "=" * 80)

# Test case with multiple lists
print("\nTest case with multiple horizontal lists:")

# Create: 2 -> 4 -> 6
#         |    |    |
#         3    5    7
node2 = Node(2)
node4 = Node(4)
node6 = Node(6)
node2.next = node4
node4.next = node6

node3 = Node(3)
node5 = Node(5)
node7 = Node(7)
node2.bottom = node3
node4.bottom = node5
node6.bottom = node7

flattened_multi = flatten(node2)
print("Flattened list:")
print_flattened_list(flattened_multi)
print("Expected: 2 -> 3 -> 4 -> 5 -> 6 -> 7")