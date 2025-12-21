#### https://leetcode.com/problems/linked-list-cycle-ii/


Take two pointers, fast and slow. Fast goes two steps ahead while slow pointer does single step ahead for each iteration. If a cycle exists, fast and slow pointers will collide. 
Take another pointer, say check. Move the slow and the check pointers ahead by single steps until they collide. Once they collide we get the starting node of the linked list


Proof of Why check and slow will collide at the node where loop started.↓ 👇
<a href="#"><img width="100%" height="50%" src="https://raw.githubusercontent.com/SamirPaulb/assets/main/LinkedList-Cycle-II-find-point-where-loop-started.jpg" /></a>

```python

# https://leetcode.com/problems/linked-list-cycle-ii/

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        # Step 1: Detect cycle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                break
        else:
            return None   # No cycle

        # Step 2: Find start of cycle
        check = head
        while check != slow:
            check = check.next
            slow = slow.next

        return check


# ---------------- DRIVER CODE ----------------
if __name__ == "__main__":
    sol = Solution()

    # Create linked list: 3 -> 2 -> 0 -> -4 -> (cycle to index 1)
    n1 = ListNode(3)
    n2 = ListNode(2)
    n3 = ListNode(0)
    n4 = ListNode(-4)

    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n2   # cycle starts at node with value 2

    result = sol.detectCycle(n1)

    print(result.val if result else None)
    # Expected Output: 2


    # -------- No cycle case --------
    a1 = ListNode(1)
    a2 = ListNode(2)
    a3 = ListNode(3)

    a1.next = a2
    a2.next = a3

    result2 = sol.detectCycle(a1)

    print(result2.val if result2 else None)
    # Expected Output: None


# Time: O(N)
# Space: O(1)
```
