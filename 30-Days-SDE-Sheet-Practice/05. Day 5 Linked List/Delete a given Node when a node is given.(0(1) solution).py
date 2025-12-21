# https://leetcode.com/problems/delete-node-in-a-linked-list/

'''
We are given only the node. the head is not given.
So instead of deleting the given node delete the next node of change the value of
the given node with the next node's value. 
But this approach only change the value of the given node not link with previous node.
'''

# https://leetcode.com/problems/delete-node-in-a-linked-list/

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteNode(self, node: ListNode) -> None:
        """
        We are NOT given head.
        Copy next node's value into current node
        and bypass the next node.
        """
        node.val = node.next.val
        node.next = node.next.next


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

    # Create linked list: 4 -> 5 -> 1 -> 9
    head = create_linked_list([4, 5, 1, 9])

    print("Original List:")
    print_linked_list(head)

    # Suppose we are given node with value 5
    node_to_delete = head.next   # node with value 5

    sol.deleteNode(node_to_delete)

    print("After Deleting Node (5):")
    print_linked_list(head)


# Time: O(1)
# Space: O(1)
        