# https://leetcode.com/problems/copy-list-with-random-pointer/
''' 
In a dictionary store the new copy nodes. Then in another traversal connect the links of 
the new nodes. 
'''

# https://leetcode.com/problems/copy-list-with-random-pointer/

from typing import Optional

class Node:
    def __init__(self, val: int, next: 'Optional[Node]' = None, random: 'Optional[Node]' = None):
        self.val = val
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        cur = head
        oldToCopy = {None: None}

        # First pass: create copy of each node
        while cur:
            oldToCopy[cur] = Node(cur.val)
            cur = cur.next

        # Second pass: assign next and random pointers
        cur = head
        while cur:
            copy = oldToCopy[cur]
            copy.next = oldToCopy[cur.next]
            copy.random = oldToCopy[cur.random]
            cur = cur.next

        return oldToCopy[head]


# ---------------- DRIVER CODE ----------------
def print_list(head):
    res = []
    cur = head
    while cur:
        random_val = cur.random.val if cur.random else None
        res.append([cur.val, random_val])
        cur = cur.next
    print(res)


if __name__ == "__main__":
    # Creating original list:
    # 1 -> 2 -> 3
    # random pointers:
    # 1.random -> 3
    # 2.random -> 1
    # 3.random -> 2

    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)

    n1.next = n2
    n2.next = n3

    n1.random = n3
    n2.random = n1
    n3.random = n2

    sol = Solution()
    copied_head = sol.copyRandomList(n1)

    print_list(copied_head)
    # Expected Output:
    # [[1, 3], [2, 1], [3, 2]]


# Time: O(N)
# Space: O(N)