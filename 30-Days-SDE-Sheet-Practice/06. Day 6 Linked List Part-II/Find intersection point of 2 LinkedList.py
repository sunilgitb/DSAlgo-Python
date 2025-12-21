# https://leetcode.com/problems/intersection-of-two-linked-lists/

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:

        a = headA
        b = headB

        # If lists intersect, pointers will meet after at most 2 passes
        while a != b:
            a = a.next if a else headB
            b = b.next if b else headA

        return a   # intersection node or None


# ---------------- HELPER FUNCTIONS ----------------
def create_linked_list(arr):
    dummy = ListNode(0)
    cur = dummy
    for num in arr:
        cur.next = ListNode(num)
        cur = cur.next
    return dummy.next


def attach_intersection(headA, headB, pos):
    """
    pos = index in headA where headB should intersect
    pos = -1 means no intersection
    """
    if pos == -1:
        return headA, headB

    curA = headA
    for _ in range(pos):
        curA = curA.next

    curB = headB
    while curB.next:
        curB = curB.next

    curB.next = curA
    return headA, headB


def print_linked_list(head, limit=10):
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

    # -------- Test Case 1: Intersection exists --------
    headA = create_linked_list([4, 1, 8, 4, 5])
    headB = create_linked_list([5, 6, 1])

    # intersect at node with value 8 (index 2 in headA)
    headA, headB = attach_intersection(headA, headB, 2)

    print("List A:")
    print_linked_list(headA)
    print("List B:")
    print_linked_list(headB)

    intersection = sol.getIntersectionNode(headA, headB)
    print("Intersection Node Value:", intersection.val if intersection else None)

    print()

    # -------- Test Case 2: No intersection --------
    headA2 = create_linked_list([2, 6, 4])
    headB2 = create_linked_list([1, 5])

    print("List A:")
    print_linked_list(headA2)
    print("List B:")
    print_linked_list(headB2)

    intersection2 = sol.getIntersectionNode(headA2, headB2)
    print("Intersection Node Value:", intersection2.val if intersection2 else None)
