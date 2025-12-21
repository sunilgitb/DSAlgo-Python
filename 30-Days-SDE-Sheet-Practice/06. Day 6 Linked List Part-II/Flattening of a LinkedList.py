# https://practice.geeksforgeeks.org/problems/flattening-a-linked-list/1

''' 
Select 2 bottom directed linklist at a time and use the concept of "21. Merge Two Sorted Lists"
on them. Start traversing from the begining. Assign 'a' linkedList wirh smaller head and
'b' to the larger head. Change main head to a. At the end we will have the sorted Linkedlist with only bottom pointer.

Input:
a     b     c           => take 'a' at smaller head
5 -> 10 -> 19 -> 28
|     |     |     | 
7     20    22   35
|           |     | 
8          50    40
|                 | 
30               45

Output:  5-> 7-> 8- > 10 -> 19-> 20-> 22-> 28-> 30-> 35-> 40-> 45-> 50 bottom pointer

'''


'''
class Node:
    def __init__(self, d):
        self.data=d
        self.next=None
        self.bottom=None
'''

# https://practice.geeksforgeeks.org/problems/flattening-a-linked-list/1

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.bottom = None


def flatten(head):
    if not head:
        return head

    # Merge lists one by one
    while head.next:
        a = head
        b = head.next

        # Merge two sorted bottom-linked lists
        while a and b:
            if not a.bottom:
                a.bottom = b
                break
            if a.bottom.data > b.data:
                a.bottom, b = b, a.bottom
            a = a.bottom

        head.next = head.next.next

    return head


def printBottom(head):
    while head:
        print(head.data, end=" ")
        head = head.bottom
    print()


# ---------------- DRIVER CODE ----------------
if __name__ == "__main__":

    # Creating the linked list shown in the example

    # a -> b -> c -> d
    head = Node(5)
    head.next = Node(10)
    head.next.next = Node(19)
    head.next.next.next = Node(28)

    # bottom links
    head.bottom = Node(7)
    head.bottom.bottom = Node(8)
    head.bottom.bottom.bottom = Node(30)

    head.next.bottom = Node(20)

    head.next.next.bottom = Node(22)
    head.next.next.bottom.bottom = Node(50)

    head.next.next.next.bottom = Node(35)
    head.next.next.next.bottom.bottom = Node(40)
    head.next.next.next.bottom.bottom.bottom = Node(45)

    flat = flatten(head)

    printBottom(flat)
    # Expected Output:
    # 5 7 8 10 19 20 22 28 30 35 40 45 50

                

# Time Complexity: O(N*N*M)
# Auxiliary Space: O(1)
