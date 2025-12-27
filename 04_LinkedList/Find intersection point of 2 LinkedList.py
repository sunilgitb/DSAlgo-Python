from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None
            
        a = headA
        b = headB
        
        while a != b:
            a = a.next if a else headB
            b = b.next if b else headA
        
        return a

def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def create_intersection(list1, list2, intersection_point):
    """Create two linked lists that intersect at a given node"""
    if not list1 or not list2:
        return list1, list2, None
    
    # Find the intersection node in list1
    node1 = list1
    for _ in range(intersection_point):
        if node1:
            node1 = node1.next
    
    # Connect list2 to the intersection node
    node2 = list2
    while node2 and node2.next:
        node2 = node2.next
    if node2 and node1:
        node2.next = node1
    
    return list1, list2, node1

# Test cases
solution = Solution()

print("Testing Intersection of Two Linked Lists:")
print("=" * 80)

# Test case 1: Intersection exists
print("\nTest 1: Lists intersect at node with value 8")
listA = create_linked_list([4, 1, 8, 4, 5])
listB = create_linked_list([5, 6, 1])
listA, listB, intersection = create_intersection(listA, listB, 2)
result = solution.getIntersectionNode(listA, listB)
print(f"Intersection node value: {result.val if result else 'None'}")
print(f"Expected: 8")
print(f"✓ Correct" if result and result.val == 8 else "✗ Incorrect")

# Test case 2: Intersection at first node
print("\nTest 2: Lists intersect at first node")
listA = create_linked_list([1, 9, 1, 2, 4])
listB = create_linked_list([3, 2])
listA, listB, intersection = create_intersection(listA, listB, 3)
result = solution.getIntersectionNode(listA, listB)
print(f"Intersection node value: {result.val if result else 'None'}")
print(f"Expected: 2")
print(f"✓ Correct" if result and result.val == 2 else "✗ Incorrect")

# Test case 3: No intersection
print("\nTest 3: No intersection")
listA = create_linked_list([2, 6, 4])
listB = create_linked_list([1, 5])
result = solution.getIntersectionNode(listA, listB)
print(f"Intersection node value: {result.val if result else 'None'}")
print(f"Expected: None")
print(f"✓ Correct" if result is None else "✗ Incorrect")

# Test case 4: Same list (identical)
print("\nTest 4: Same list")
listA = create_linked_list([1, 2, 3, 4, 5])
result = solution.getIntersectionNode(listA, listA)
print(f"Intersection node value: {result.val if result else 'None'}")
print(f"Expected: 1 (head of list)")
print(f"✓ Correct" if result and result.val == 1 else "✗ Incorrect")

# Test case 5: Empty lists
print("\nTest 5: One empty list")
listA = create_linked_list([1, 2, 3])
listB = None
result = solution.getIntersectionNode(listA, listB)
print(f"Intersection node value: {result.val if result else 'None'}")
print(f"Expected: None")
print(f"✓ Correct" if result is None else "✗ Incorrect")

# Test case 6: Lists intersect at last node
print("\nTest 6: Lists intersect at last node")
listA = create_linked_list([1, 2, 3, 4, 5])
listB = create_linked_list([6, 7, 8, 9])
listA, listB, intersection = create_intersection(listA, listB, 4)  # Last node
result = solution.getIntersectionNode(listA, listB)
print(f"Intersection node value: {result.val if result else 'None'}")
print(f"Expected: 5")
print(f"✓ Correct" if result and result.val == 5 else "✗ Incorrect")

# Test case 7: Circular reference check
print("\nTest 7: Lists of different lengths")
listA = create_linked_list([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21])
listB = create_linked_list([2, 4, 6])
listA, listB, intersection = create_intersection(listA, listB, 5)  # Intersect at value 11
result = solution.getIntersectionNode(listA, listB)
print(f"Intersection node value: {result.val if result else 'None'}")
print(f"Expected: 11")
print(f"✓ Correct" if result and result.val == 11 else "✗ Incorrect")

print("\n" + "=" * 80)
print("All tests completed!")