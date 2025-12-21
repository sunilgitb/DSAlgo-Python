# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

''' 
Take a dummy node connect it with head (if we take a dummy node then it would be easy 
to delete the first node if target node is head ie. n = length of list). 
Take 2 pointers fast and slow. Increase the fast pointer by n steps. 
Then in next pass increase both slow and fast together by one step. 
Slow will stop before the target element then delete the link.
'''
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head

        fast = head
        slow = dummy

        # move fast pointer n steps ahead
        for _ in range(n):
            fast = fast.next

        # move both pointers until fast reaches end
        while fast:
            fast = fast.next
            slow = slow.next

        # delete nth node from end
        slow.next = slow.next.next

        return dummy.next


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
    n = 2

    head = create_linked_list(arr)

    print("Original Linked List:")
    print_linked_list(head)

    head = sol.removeNthFromEnd(head, n)

    print(f"\nLinked List after removing {n}th node from end:")
    print_linked_list(head)


# Time: O(N)   where N is the length of the linkedlist 
# Space: O(1)
