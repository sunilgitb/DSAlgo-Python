class Node:
    def __init__(self, data):
        self.data = data
        self.nref = None
        self.pref = None

class DoublyLL:
    def __init__(self):
        self.head = None

    def print_ll(self):
        if self.head is None:
            print("The Doubly linked list is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data, end=" <-> ")
                n = n.nref
            print("None")

    def print_ll_reverse(self):
        if self.head is None:
            print("The Doubly linked list is empty")
        else:
            n = self.head 
            while n.nref is not None:
                n = n.nref
            while n is not None:
                print(n.data, end=" <-> ")
                n = n.pref
            print("None")

    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            n.nref = new_node
            new_node.pref = n
    
    def add_begin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.nref = self.head
            self.head.pref = new_node
            self.head = new_node

    def add_after_node(self, data, x):
        new_node = Node(data)
        n = self.head
        while n is not None:
            if n.data == x:
                break
            n = n.nref
        if n is None:
            print(f"We can't add after {x}, node not found")
        else:
            if n.nref is None:
                n.nref = new_node
                new_node.pref = n
            else:
                new_node.nref = n.nref
                n.nref.pref = new_node
                n.nref = new_node
                new_node.pref = n

    def add_before_node(self, data, x):
        if self.head is None:
            print("Linked List is Empty!")
            return
        if self.head.data == x:
            new_node = Node(data)
            self.head.pref = new_node
            new_node.nref = self.head
            self.head = new_node            
            return
        n = self.head
        while n.nref is not None:
            if x == n.nref.data:
                break
            n = n.nref
        if n.nref is None:
            print(f"Node {x} is not present in Linked List!")
        else:
            new_node = Node(data)
            new_node.pref = n
            new_node.nref = n.nref
            n.nref.pref = new_node            
            n.nref = new_node

    def delete_begine(self):
        if self.head is None:
            print("DLL is empty so can't delete")
            return
        if self.head.nref == None:
            self.head = None
            return
        else:
            self.head = self.head.nref
            self.head.pref = None

    def delete_end(self):
        if self.head is None:
            print("DLL is empty so can't delete")
            return
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            n.pref.nref = None

    def delete_by_value(self, x):
        if self.head is None:
            print("DLL is empty so can't delete")
            return
        if self.head.nref is None:
            if self.head.data == x:
                self.head = None
            else:
                print(f"Value {x} is not present")
            return
        if self.head.data == x:
            self.head = self.head.nref
            self.head.pref = None
            return
        else:
            n = self.head
            while n.nref is not None:
                if n.data == x:
                    break
                n = n.nref
            if n.nref is not None:
                n.nref.pref = n.pref
                n.pref.nref = n.nref
            else:
                if n.data == x:
                    n.pref.nref = None
                else:
                    print(f"Can't delete {x} as it is not present")


print("Testing Doubly Linked List Operations:")
print("=" * 60)

DLL = DoublyLL()

print("\n1. Adding 20 at beginning:")
DLL.add_begin(20)
DLL.print_ll()

print("\n2. Adding 10 at beginning:")
DLL.add_begin(10)
DLL.print_ll()

print("\n3. Adding 50 at end:")
DLL.add_end(50)
DLL.print_ll()

print("\n4. Adding 30 after node 20:")
DLL.add_after_node(30, 20)
DLL.print_ll()

print("\n5. Adding 40 before node 50:")
DLL.add_before_node(40, 50)
DLL.print_ll()

print("\n6. Deleting beginning node:")
DLL.delete_begine()
DLL.print_ll()

print("\n7. Deleting end node:")
DLL.delete_end()
DLL.print_ll()

print("\n8. Trying to delete non-existent node 100:")
DLL.delete_by_value(100)
DLL.print_ll()

print("\n9. Current list forward:")
DLL.print_ll()

print("\n10. Current list reverse:")
DLL.print_ll_reverse()

print("\n" + "=" * 60)
print("Additional operations:")

print("\n11. Deleting node 30:")
DLL.delete_by_value(30)
DLL.print_ll()

print("\n12. Adding 60 before node 40:")
DLL.add_before_node(60, 40)
DLL.print_ll()

print("\n13. Adding 70 after node 20:")
DLL.add_after_node(70, 20)
DLL.print_ll()

print("\n14. Final list forward:")
DLL.print_ll()

print("\n15. Final list reverse:")
DLL.print_ll_reverse()