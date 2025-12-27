from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-5001)
        dummy.next = head
        pre = head
        cur = pre.next if head else None
        
        while cur:
            if pre.val <= cur.val:
                pre = cur
                cur = cur.next
                continue
                
            tmp = dummy
            while cur.val > tmp.next.val:
                tmp = tmp.next
            pre.next = cur.next
            cur.next = tmp.next
            tmp.next = cur
            cur = pre.next
        
        return dummy.next

def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def linked_list_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

# Test cases
solution = Solution()

test_cases = [
    [4, 2, 1, 3],
    [-1, 5, 3, 4, 0],
    [1],
    [],
    [5, 4, 3, 2, 1],
    [1, 2, 3, 4, 5],
    [3, 7, 4, 9, 5, 2, 6, 1]
]

print("Testing Insertion Sort on Linked List:")
print("=" * 60)

for i, test_arr in enumerate(test_cases, 1):
    head = create_linked_list(test_arr)
    print(f"\nTest {i}:")
    print(f"Original list: {test_arr}")
    
    sorted_head = solution.insertionSortList(head)
    sorted_list = linked_list_to_list(sorted_head)
    
    print(f"Sorted list:   {sorted_list}")
    
    # Verify the list is sorted
    is_sorted = all(sorted_list[i] <= sorted_list[i+1] for i in range(len(sorted_list)-1)) if sorted_list else True
    print(f"✓ Correctly sorted" if is_sorted else f"✗ Not correctly sorted")