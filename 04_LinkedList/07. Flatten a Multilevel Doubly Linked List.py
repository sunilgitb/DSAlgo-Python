class Node:
    def __init__(self, val, prev=None, next=None, child=None):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
            
        def solve(node):
            tail = node
            while node:
                nxt = node.next
                if not nxt:
                    tail = node
                    
                if node.child:
                    node.next = node.child
                    node.child.prev = node
                    child_tail = solve(node.child)
                    
                    child_tail.next = nxt
                    if nxt:
                        nxt.prev = child_tail
                    
                    node.child = None
                    node = child_tail
                else:
                    node = node.next
            return tail
        
        solve(head)
        return head

def create_multilevel_list():
    # Level 0: 1 <-> 2 <-> 3 <-> 4 <-> 5 <-> 6
    #            |
    # Level 1:   7 <-> 8 <-> 9 <-> 10
    #                     |
    # Level 2:          11 <-> 12
    
    # Level 2
    node11 = Node(11)
    node12 = Node(12)
    node11.next = node12
    node12.prev = node11
    
    # Level 1
    node7 = Node(7)
    node8 = Node(8)
    node9 = Node(9)
    node10 = Node(10)
    
    node7.next = node8
    node8.prev = node7
    node8.next = node9
    node9.prev = node8
    node9.next = node10
    node10.prev = node9
    node8.child = node11  # Level 2 attached to node8
    
    # Level 0
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)
    
    node1.next = node2
    node2.prev = node1
    node2.next = node3
    node3.prev = node2
    node3.next = node4
    node4.prev = node3
    node4.next = node5
    node5.prev = node4
    node5.next = node6
    node6.prev = node5
    
    node2.child = node7  # Level 1 attached to node2
    
    return node1

def print_list(head):
    result = []
    while head:
        result.append(str(head.val))
        head = head.next
    print(" <-> ".join(result))

# Test the solution
solution = Solution()

print("Testing Flatten Multilevel Doubly Linked List:")
print("=" * 80)

print("\nOriginal multilevel list structure:")
print("Level 0: 1 <-> 2 <-> 3 <-> 4 <-> 5 <-> 6")
print("           |")
print("Level 1:   7 <-> 8 <-> 9 <-> 10")
print("                |")
print("Level 2:      11 <-> 12")

head = create_multilevel_list()
flattened = solution.flatten(head)

print("\nFlattened list (depth-first traversal):")
print_list(flattened)
print("Expected: 1 <-> 2 <-> 7 <-> 8 <-> 11 <-> 12 <-> 9 <-> 10 <-> 3 <-> 4 <-> 5 <-> 6")

print("\n" + "=" * 80)
print("\nAdditional test cases:")

# Test case 2: Single node with child
node1 = Node(1)
node2 = Node(2)
node1.child = node2

flattened2 = solution.flatten(node1)
print("\nTest 2: Single node with child")
print_list(flattened2)
print("Expected: 1 <-> 2")

# Test case 3: No child nodes
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node1.next = node2
node2.prev = node1
node2.next = node3
node3.prev = node2

flattened3 = solution.flatten(node1)
print("\nTest 3: No child nodes")
print_list(flattened3)
print("Expected: 1 <-> 2 <-> 3")

# Test case 4: Empty list
flattened4 = solution.flatten(None)
print("\nTest 4: Empty list")
print_list(flattened4)
print("Expected: (empty)")

# Test case 5: Multiple levels deep
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)

node1.next = node2
node2.prev = node1
node2.child = node3
node3.next = node4
node4.prev = node3
node4.child = node5
node5.next = node6
node6.prev = node5

flattened5 = solution.flatten(node1)
print("\nTest 5: Multiple levels deep")
print_list(flattened5)
print("Expected: 1 <-> 2 <-> 3 <-> 4 <-> 5 <-> 6")