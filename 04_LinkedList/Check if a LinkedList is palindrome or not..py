from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True
        
        # Find middle       
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Reverse LinkedList right-side of middle
        pre = slow
        cur = pre.next
        nex = cur.next
        
        while nex:
            cur.next = nex.next
            nex.next = pre.next
            pre.next = nex
            nex = cur.next
        
        # Check equality of values
        left = head
        right = slow.next
        while left and right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        
        return True

def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Test cases
solution = Solution()

test_cases = [
    [1, 2, 2, 1],      # True
    [1, 2, 3, 2, 1],   # True
    [1, 2, 3, 4, 5],   # False
    [1, 2, 3, 3, 2, 1], # True
    [1],               # True
    [1, 2],            # False
    [1, 1],            # True
    [1, 2, 1],         # True
    [],                # True (empty list)
]

print("Testing Palindrome Linked List:")
print("=" * 60)

for i, test_arr in enumerate(test_cases, 1):
    head = create_linked_list(test_arr)
    result = solution.isPalindrome(head)
    expected = test_arr == test_arr[::-1] if test_arr else True
    
    print(f"Test {i}: {test_arr}")
    print(f"Result: {result}, Expected: {expected}")
    print(f"{'✓' if result == expected else '✗'}")
    print("-" * 40)