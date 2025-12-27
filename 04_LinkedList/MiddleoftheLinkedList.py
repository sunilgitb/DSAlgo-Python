from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # Method 1: Fast and slow pointers
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    # Method 2: Count length
    def middleNode_count(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        length = 0
        while cur:
            length += 1
            cur = cur.next
        
        mid = length // 2
        cur = head
        for _ in range(mid):
            cur = cur.next
        return cur

def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def print_linked_list(head):
    result = []
    while head:
        result.append(str(head.val))
        head = head.next
    print(" -> ".join(result) + " -> None")

# Test cases
solution = Solution()

test_cases = [
    [1, 2, 3, 4, 5],      # Middle: 3
    [1, 2, 3, 4, 5, 6],   # Middle: 4
    [1],                  # Middle: 1
    [1, 2],               # Middle: 2
    [1, 2, 3],            # Middle: 2
    [1, 2, 3, 4],         # Middle: 3
    [],                   # Middle: None
]

print("Testing Middle of the Linked List:")
print("=" * 60)

for i, test_arr in enumerate(test_cases, 1):
    head = create_linked_list(test_arr)
    
    print(f"\nTest {i}:")
    print(f"List: {test_arr}")
    
    if test_arr:
        # Method 1
        middle1 = solution.middleNode(head)
        middle_val1 = middle1.val if middle1 else None
        
        # Method 2
        head = create_linked_list(test_arr)  # Reset head
        middle2 = solution.middleNode_count(head)
        middle_val2 = middle2.val if middle2 else None
        
        # Expected middle
        if test_arr:
            expected_index = len(test_arr) // 2
            expected_val = test_arr[expected_index]
        else:
            expected_val = None
        
        print(f"Method 1 (fast/slow): {middle_val1}")
        print(f"Method 2 (count):     {middle_val2}")
        print(f"Expected:             {expected_val}")
        
        if middle_val1 == middle_val2 == expected_val:
            print("✓ Both methods correct")
        else:
            print("✗ Methods differ or incorrect")
    else:
        print("Empty list - both methods should return None")
        middle1 = solution.middleNode(head)
        middle2 = solution.middleNode_count(head)
        print(f"Method 1: {middle1}")
        print(f"Method 2: {middle2}")
        print("✓ Both return None for empty list" if middle1 is None and middle2 is None else "✗ Error")

print("\n" + "=" * 60)
print("\nDetailed example with longer list:")

long_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
head = create_linked_list(long_list)

print(f"\nList of length {len(long_list)}:")
print_linked_list(head)

middle1 = solution.middleNode(head)
head = create_linked_list(long_list)  # Reset
middle2 = solution.middleNode_count(head)

print(f"\nMiddle node value (both methods): {middle1.val}")
print(f"Middle node is at index {len(long_list)//2} (0-based)")
print(f"Nodes from middle to end:")
current = middle1
while current:
    print(current.val, end=" -> ")
    current = current.next
print("None")