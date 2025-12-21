# https://leetcode.com/problems/middle-of-the-linked-list/

# https://leetcode.com/problems/middle-of-the-linked-list/

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        return slow


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

    print("Linked List:")
    print_linked_list(head)

    mid = sol.middleNode(head)

    print("Middle Node Value:")
    print(mid.val)

    print("Middle to End:")
    print_linked_list(mid)


# Time: O(N)
# Space: O(1)