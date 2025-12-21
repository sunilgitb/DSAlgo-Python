# https://leetcode.com/problems/is-graph-bipartite/

'''
A graph is bipartite if the nodes can be partitioned into two independent sets A and B such that
all the edges are connected across A and B. If there is a edge within A or B then that graph is Not bipartite.
            0
          /   \
         1     2
         |     |
         3-----4
A = {0, 3, 4}; B = {1, 2}    => node 3 and 4 are connected within set A. so not bipartite

1. All acyclic graphs are Bipartite.
2. Cyclic graph of elven length is Bipartite.
3. Acyclic graph of odd lenght is Not Bipartite.

To find cyclic and acyclic we will keep a dictionay with key as node and value as it's colour. 
If current node is seen previously and it's previous colour is different then it is a cyclic graph with Odd lenght.
'''

import collections
from typing import List

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        seen = {}  # key: node, value: color (1 or -1)

        for node in range(len(graph)):  # handle disconnected components
            if node not in seen:
                q = collections.deque([(node, 1)])

                while q:
                    curr, color = q.popleft()

                    if curr in seen:
                        if seen[curr] == color:
                            continue
                        else:
                            return False  # odd-length cycle
                    seen[curr] = color

                    for nei in graph[curr]:
                        q.append((nei, -color))

        return True


# ---------------- DRIVER CODE ----------------
if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        ([[1,3],[0,2],[1,3],[0,2]], True),     # Bipartite (even cycle)
        ([[1,2,3],[0,2],[0,1,3],[0,2]], False),# Not bipartite (odd cycle)
        ([[1],[0,3],[3],[1,2]], True),         # Disconnected bipartite
        ([[],[2,4],[1],[4],[1,3]], True),      # Multiple components
        ([[1],[0,2],[1]], True)                # Simple chain
    ]

    for i, (graph, expected) in enumerate(test_cases, 1):
        result = sol.isBipartite(graph)
        print(f"Test Case {i}:")
        print(f"Graph: {graph}")
        print(f"Output: {result}, Expected: {expected}")
        print("-" * 40)


# Time = number of nodes + number of edges
# Time: O(n) + O(n)
# Space: O(n) + o(n)  
# Auxiliary Space: O(n)
