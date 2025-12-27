class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, new_value):
        new_node = Node(new_value)
        
        if self.head is None:
            self.head = new_node
            return
        
        curr_node = self.head
        while curr_node.next is not None:
            curr_node = curr_node.next
            
        curr_node.next = new_node
    
    def sortedMerge(self, a, b):
        if a == None:
            return b
        if b == None:
            return a
            
        if a.data <= b.data:
            result = a
            result.next = self.sortedMerge(a.next, b)
        else:
            result = b
            result.next = self.sortedMerge(a, b.next)
        return result
    
    def mergeSort(self, h):
        if h == None or h.next == None:
            return h

        middle = self.getMiddle(h)
        nexttomiddle = middle.next

        middle.next = None

        left = self.mergeSort(h)
        right = self.mergeSort(nexttomiddle)

        sortedlist = self.sortedMerge(left, right)
        return sortedlist
    
    def getMiddle(self, head):
        if head == None:
            return head

        slow = head
        fast = head

        while fast.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next
            
        return slow

def printList(head):
    if head is None:
        print('Empty List')
        return
    curr_node = head
    while curr_node:
        print(curr_node.data, end=" -> ")
        curr_node = curr_node.next
    print("None")


# Test cases
print("Testing Merge Sort on Linked List:")
print("=" * 60)

# Test case 1
print("\nTest case 1:")
li1 = LinkedList()
li1.append(15)
li1.append(10)
li1.append(5)
li1.append(20)
li1.append(3)
li1.append(2)

print("Original Linked List:")
printList(li1.head)

li1.head = li1.mergeSort(li1.head)
print("Sorted Linked List:")
printList(li1.head)

# Test case 2
print("\n" + "=" * 60)
print("Test case 2:")
li2 = LinkedList()
li2.append(64)
li2.append(34)
li2.append(25)
li2.append(12)
li2.append(22)
li2.append(11)
li2.append(90)

print("Original Linked List:")
printList(li2.head)

li2.head = li2.mergeSort(li2.head)
print("Sorted Linked List:")
printList(li2.head)

# Test case 3
print("\n" + "=" * 60)
print("Test case 3 (single element):")
li3 = LinkedList()
li3.append(42)

print("Original Linked List:")
printList(li3.head)

li3.head = li3.mergeSort(li3.head)
print("Sorted Linked List:")
printList(li3.head)

# Test case 4
print("\n" + "=" * 60)
print("Test case 4 (empty list):")
li4 = LinkedList()

print("Original Linked List:")
printList(li4.head)

li4.head = li4.mergeSort(li4.head)
print("Sorted Linked List:")
printList(li4.head)

# Test case 5
print("\n" + "=" * 60)
print("Test case 5 (already sorted):")
li5 = LinkedList()
li5.append(1)
li5.append(2)
li5.append(3)
li5.append(4)
li5.append(5)

print("Original Linked List:")
printList(li5.head)

li5.head = li5.mergeSort(li5.head)
print("Sorted Linked List:")
printList(li5.head)

# Test case 6
print("\n" + "=" * 60)
print("Test case 6 (reverse sorted):")
li6 = LinkedList()
li6.append(5)
li6.append(4)
li6.append(3)
li6.append(2)
li6.append(1)

print("Original Linked List:")
printList(li6.head)

li6.head = li6.mergeSort(li6.head)
print("Sorted Linked List:")
printList(li6.head)