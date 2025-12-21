# https://leetcode.com/problems/linked-list-cycle/

# https://leetcode.com/problems/linked-list-cycle/

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False


# ---------------- HELPER FUNCTIONS ----------------
def create_linked_list(arr):
    dummy = ListNode(0)
    cur = dummy
    for num in arr:
        cur.next = ListNode(num)
        cur = cur.next
    return dummy.next


def create_cycle(head, pos):
    """
    pos = index where tail connects (0-based)
    pos = -1 means no cycle
    """
    if pos == -1:
        return head

    cycle_node = None
    cur = head
    idx = 0

    while cur.next:
        if idx == pos:
            cycle_node = cur
        cur = cur.next
        idx += 1

    cur.next = cycle_node
    return head


def print_linked_list(head, limit=15):
    """
    Prints list safely (limited nodes to avoid infinite loop)
    """
    res = []
    count = 0
    while head and count < limit:
        res.append(str(head.val))
        head = head.next
        count += 1

    if head:
        res.append("...")
    print(" -> ".join(res))


# ---------------- DRIVER CODE ----------------
if __name__ == "__main__":
    sol = Solution()

    # -------- Test Case 1: Cycle exists --------
    arr1 = [3, 2, 0, -4]
    head1 = create_linked_list(arr1)
    head1 = create_cycle(head1, 1)  # tail connects to index 1

    print("Linked List (with cycle):")
    print_linked_list(head1)
    print("Has Cycle?", sol.hasCycle(head1))

    print()

    # -------- Test Case 2: No cycle --------
    arr2 = [1, 2, 3, 4]
    head2 = create_linked_list(arr2)

    print("Linked List (no cycle):")
    print_linked_list(head2)
    print("Has Cycle?", sol.hasCycle(head2))

    
# Time: O(n)
# Space: O(1)