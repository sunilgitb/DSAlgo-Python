# https://leetcode.com/problems/palindrome-linked-list/

'''
Go to the middle node and reverse the right-side linkedlist.
Then take 2 pointers one from start and another from middle and check
equality of value.
'''

# https://leetcode.com/problems/palindrome-linked-list/

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True

        # ---------- Step 1: Find middle ----------
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # slow is the node before the middle

        # ---------- Step 2: Reverse right half ----------
        pre = slow
        cur = pre.next
        nex = cur.next

        while nex:
            cur.next = nex.next
            nex.next = pre.next
            pre.next = nex
            nex = cur.next

        # ---------- Step 3: Compare both halves ----------
        left = head
        right = slow.next

        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next

        return True


# ---------------- HELPER FUNCTIONS ----------------
def create_linked_list(arr):
    dummy = ListNode(0)
    cur = dummy
    for num in arr:
        cur.next = ListNode(num)
        cur = cur.next
    return dummy.next


def print_linked_list(head):
    res = []
    while head:
        res.append(str(head.val))
        head = head.next
    print(" -> ".join(res))


# ---------------- DRIVER CODE ----------------
if __name__ == "__main__":
    sol = Solution()

    # Test Case 1
    arr1 = [1, 2, 2, 1]
    head1 = create_linked_list(arr1)

    print("Linked List:")
    print_linked_list(head1)
    print("Is Palindrome?", sol.isPalindrome(head1))

    print()

    # Test Case 2
    arr2 = [1, 2, 3, 2, 1]
    head2 = create_linked_list(arr2)

    print("Linked List:")
    print_linked_list(head2)
    print("Is Palindrome?", sol.isPalindrome(head2))

    print()

    # Test Case 3
    arr3 = [1, 2, 3, 4]
    head3 = create_linked_list(arr3)

    print("Linked List:")
    print_linked_list(head3)
    print("Is Palindrome?", sol.isPalindrome(head3))

# Time: O(N)
# Space: O(1)