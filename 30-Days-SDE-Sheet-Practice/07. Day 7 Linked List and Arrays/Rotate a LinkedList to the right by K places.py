# https://leetcode.com/problems/rotate-list/
''' 
With 2 pointer approach go to the (length - K)th node the disconnect right part
and connect it to the front head. return the new head(ie. node where we disconnected)  
'''
# https://leetcode.com/problems/rotate-list/

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head

        # find length
        cur = head
        length = 1
        while cur.next:
            cur = cur.next
            length += 1

        k = k % length
        if k == 0:
            return head

        # make circular list
        cur.next = head

        # find new tail: (length - k - 1)
        steps = length - k
        new_tail = head
        for _ in range(steps - 1):
            new_tail = new_tail.next

        new_head = new_tail.next
        new_tail.next = None

        return new_head


# ---------------- DRIVER CODE ----------------
def printList(head):
    res = []
    while head:
        res.append(head.val)
        head = head.next
    print(res)


if __name__ == "__main__":
    sol = Solution()

    # Test Case 1
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    head = sol.rotateRight(head, 2)
    printList(head)
    # Expected Output: [4, 5, 1, 2, 3]

    # Test Case 2
    head = ListNode(0, ListNode(1, ListNode(2)))
    head = sol.rotateRight(head, 4)
    printList(head)
    # Expected Output: [2, 0, 1]

    # Test Case 3
    head = ListNode(1)
    head = sol.rotateRight(head, 10)
    printList(head)
    # Expected Output: [1]

    
# Time: O(N)
# Space: (1)