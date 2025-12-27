class Node:
    def __init__(self, my_data):
        self.data = my_data
        self.next = None

class circularLinkedList:  
    def __init__(self):
        self.head = None
    
    def add_data(self, my_data):
        ptr_1 = Node(my_data)
        temp = self.head    
        ptr_1.next = self.head

        if self.head is not None:
            while temp.next != self.head:
                temp = temp.next
            temp.next = ptr_1
        else:
            ptr_1.next = ptr_1
        self.head = ptr_1

    def print_it(self):
        if self.head is None:
            print("Circular Linked List is empty")
            return
        
        temp = self.head
        result = []
        while True:
            result.append(str(temp.data))
            temp = temp.next
            if temp == self.head:
                break
        print(" -> ".join(result) + " -> (back to head)")

    def add_at_end(self, my_data):
        new_node = Node(my_data)
        if self.head is None:
            new_node.next = new_node
            self.head = new_node
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head

    def delete_node(self, key):
        if self.head is None:
            print("List is empty")
            return
        
        # Case 1: Only one node
        if self.head.next == self.head and self.head.data == key:
            self.head = None
            return
        
        # Case 2: Delete head node
        if self.head.data == key:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = self.head.next
            self.head = self.head.next
            return
        
        # Case 3: Delete middle or last node
        prev = None
        curr = self.head
        while True:
            if curr.data == key:
                break
            prev = curr
            curr = curr.next
            if curr == self.head:
                print(f"Node with value {key} not found")
                return
        
        prev.next = curr.next


# Test the circular linked list
print("Testing Circular Linked List:")
print("=" * 50)

my_list = circularLinkedList()

print("\n1. Adding elements at beginning:")
my_list.add_data(56)
my_list.add_data(78)
my_list.add_data(12)
print("The circular linked list is:")
my_list.print_it()

print("\n2. Adding 99 at the end:")
my_list.add_at_end(99)
my_list.print_it()

print("\n3. Adding 42 at beginning:")
my_list.add_data(42)
my_list.print_it()

print("\n4. Deleting node with value 12:")
my_list.delete_node(12)
my_list.print_it()

print("\n5. Deleting node with value 42 (head node):")
my_list.delete_node(42)
my_list.print_it()

print("\n6. Trying to delete non-existent node 100:")
my_list.delete_node(100)
my_list.print_it()

print("\n7. Deleting node with value 56:")
my_list.delete_node(56)
my_list.print_it()

print("\n8. Adding more elements:")
my_list.add_data(10)
my_list.add_data(20)
my_list.add_data(30)
my_list.add_at_end(40)
my_list.print_it()

print("\n9. Final traversal (showing circular nature):")
print("Traversing 10 nodes (even though list has fewer):")
if my_list.head:
    temp = my_list.head
    for i in range(10):
        print(temp.data, end=" -> ")
        temp = temp.next
        if i < 9:
            print("...", end=" ")
    print("(back to start)")