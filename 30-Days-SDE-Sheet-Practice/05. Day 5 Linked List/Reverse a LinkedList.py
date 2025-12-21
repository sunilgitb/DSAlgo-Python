# https://leetcode.com/problems/reverse-linked-list/
''' 
Use three pointers to change the links between nodes.
'''

# https://leetcode.com/problems/reverse-linked-list/

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        pre = ListNode(-1)
        pre.next = head
        cur = pre.next
        nex = cur.next

        while nex:
            cur.next = nex.next
            nex.next = pre.next
            pre.next = nex
            nex = cur.next

        return pre.next


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

    arr = [1, 2, 3, 4, 5]
    head = create_linked_list(arr)

    print("Original Linked List:")
    print_linked_list(head)

    head = sol.reverseList(head)

    print("\nReversed Linked List:")
    print_linked_list(head)


