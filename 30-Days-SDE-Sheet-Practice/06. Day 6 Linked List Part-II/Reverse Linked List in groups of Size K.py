# https://leetcode.com/problems/reverse-nodes-in-k-group/
''' 
Apply the concept of reverse LinkedList in a range of length K.
'''

# https://leetcode.com/problems/reverse-nodes-in-k-group/
'''
Apply the concept of reverse LinkedList in a range of length K.
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head
        cur = head
        count = 0

        # count total nodes
        while cur:
            count += 1
            cur = cur.next

        pre = dummy
        while count >= k:
            cur = pre.next
            nex = cur.next
            for _ in range(k - 1):
                cur.next = nex.next
                nex.next = pre.next
                pre.next = nex
                nex = cur.next
            pre = cur
            count -= k

        return dummy.next


# ---------------- DRIVER CODE ----------------
def printList(head):
    while head:
        print(head.val, end=" ")
        head = head.next
    print()


if __name__ == "__main__":
    # Input: 1 -> 2 -> 3 -> 4 -> 5, k = 2
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    k = 2
    sol = Solution()
    result = sol.reverseKGroup(head, k)

    printList(result)
    # Expected Output:
    # 2 1 4 3 5


# Time: O(N)
# Space: O(1)