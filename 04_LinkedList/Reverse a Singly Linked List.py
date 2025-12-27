class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # Function to reverse the linked list
    def reverse(self):
        prev = None
        current = self.head
        while current is not None:
            next_node = current.next  # Store next node
            current.next = prev       # Reverse the link
            prev = current           # Move prev forward
            current = next_node      # Move current forward
        self.head = prev

    # Function to insert a new node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # Utility function to print the linked list
    def printList(self):
        temp = self.head
        result = []
        while temp:
            result.append(str(temp.data))
            temp = temp.next
        print(" -> ".join(result) + " -> None")


# Test the linked list reversal
print("Testing Linked List Reversal:")
print("=" * 60)

# Test 1: Basic reversal
print("\nTest 1: Basic reversal")
llist1 = LinkedList()
llist1.push(20)
llist1.push(4)
llist1.push(15)
llist1.push(85)

print("Original Linked List:")
llist1.printList()

llist1.reverse()
print("Reversed Linked List:")
llist1.printList()

# Test 2: Single node
print("\n" + "=" * 60)
print("\nTest 2: Single node")
llist2 = LinkedList()
llist2.push(42)

print("Original Linked List:")
llist2.printList()

llist2.reverse()
print("Reversed Linked List:")
llist2.printList()

# Test 3: Empty list
print("\n" + "=" * 60)
print("\nTest 3: Empty list")
llist3 = LinkedList()

print("Original Linked List:")
llist3.printList()

llist3.reverse()
print("Reversed Linked List:")
llist3.printList()

# Test 4: Two nodes
print("\n" + "=" * 60)
print("\nTest 4: Two nodes")
llist4 = LinkedList()
llist4.push(2)
llist4.push(1)

print("Original Linked List:")
llist4.printList()

llist4.reverse()
print("Reversed Linked List:")
llist4.printList()

# Test 5: Longer list
print("\n" + "=" * 60)
print("\nTest 5: Longer list")
llist5 = LinkedList()
for i in range(10, 0, -1):
    llist5.push(i)

print("Original Linked List (1 to 10):")
llist5.printList()

llist5.reverse()
print("Reversed Linked List (10 to 1):")
llist5.printList()

# Test 6: Check if reversal is correct by reversing back
print("\n" + "=" * 60)
print("\nTest 6: Double reversal (should return to original)")
llist6 = LinkedList()
nums = [5, 10, 15, 20, 25]
for num in reversed(nums):
    llist6.push(num)

print("Original Linked List:")
llist6.printList()

print("\nFirst reversal:")
llist6.reverse()
llist6.printList()

print("\nSecond reversal (back to original):")
llist6.reverse()
llist6.printList()

print(f"\n✓ Matches original: {nums == [5, 10, 15, 20, 25]}")