# https://leetcode.com/problems/merge-two-sorted-lists/
''' 
Take 2 pointers on 2 lists. compare values of pointers.
'''

# https://leetcode.com/problems/merge-two-sorted-lists/

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self,
        list1: Optional[ListNode],
        list2: Optional[ListNode]
    ) -> Optional[ListNode]:

        # if any list is empty
        if not list1 or not list2:
            return list2 or list1

        # choose starting head
        if list1.val <= list2.val:
            a, b = list1, list2
        else:
            a, b = list2, list1

        res = a  # head of merged list

        while a:
            if not a.next:
                a.next = b
                return res
            elif not b:
                return res
            elif a.next.val > b.val:
                tmp = a.next
                a.next = b
                b = tmp
            a = a.next

        return res


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

    # Create two sorted linked lists
    list1 = create_linked_list([1, 2, 4])
    list2 = create_linked_list([1, 3, 4])

    print("List 1:")
    print_linked_list(list1)

    print("List 2:")
    print_linked_list(list2)

    merged = sol.mergeTwoLists(list1, list2)

    print("Merged List:")
    print_linked_list(merged)


# Time: O(n + m)  # We are still traversing both lists entirely in the worst-case scenario
# Space: O(1)     # We are using the same lists just changing links to create our desired list. So no extra space is used. 