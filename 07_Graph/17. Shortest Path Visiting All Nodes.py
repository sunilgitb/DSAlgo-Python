# https://leetcode.com/problems/shortest-path-visiting-all-nodes/
# https://www.youtube.com/watch?v=1XkMFNvkouo

from typing import List
import collections

class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        res = 2**31  # acts like infinity

        # Try starting BFS from every node
        for i in range(n):
            curPathState = 1 << i
            q = collections.deque([(i, curPathState, 0)])
            visited = set()
            ans = 2**n

            while q:
                curNode, curPathState, pathLen = q.popleft()

                # If all nodes visited
                if curPathState == (1 << n) - 1:
                    ans = min(ans, pathLen)
                    continue

                if (curNode, curPathState) in visited:
                    continue
                visited.add((curNode, curPathState))

                for childNode in graph[curNode]:
                    childPathState = curPathState | (1 << childNode)
                    q.append((childNode, childPathState, pathLen + 1))

            res = min(res, ans)

        return res


# ---------------- DRIVER CODE ----------------
if __name__ == "__main__":
    graph = [[1,2,3],[0],[0],[0]]

    obj = Solution()
    print(obj.shortestPathLength(graph))
    # Output: 4
