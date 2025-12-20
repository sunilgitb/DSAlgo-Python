# https://leetcode.com/problems/course-schedule-ii/

from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if numCourses == 0:
            return []
        if numCourses == 1:
            return [0]

        # Build adjacency list
        adjacencyList = {i: [] for i in range(numCourses)}
        for a, b in prerequisites:
            adjacencyList[a].append(b)

        # Outbound count (indegree)
        outBound = {i: 0 for i in range(numCourses)}
        for a, b in prerequisites:
            outBound[b] += 1

        # Initialize queue with nodes having 0 outbound
        q = []
        for i in outBound:
            if outBound[i] == 0:
                q.append(i)

        ans = []
        while q:
            a = q.pop()
            ans.append(a)
            for i in adjacencyList[a]:
                outBound[i] -= 1
                if outBound[i] == 0:
                    q.append(i)

        # Detect cycle
        for i in outBound:
            if outBound[i] != 0:
                return []

        return ans[::-1]


# ---------------- DRIVER CODE ----------------
if __name__ == "__main__":
    sol = Solution()

    # Test Case 1
    numCourses = 4
    prerequisites = [[1,0],[2,0],[3,1],[3,2]]
    print("Test Case 1 Output:", sol.findOrder(numCourses, prerequisites))
    # Expected: [0,1,2,3] or [0,2,1,3]

    # Test Case 2 (Cycle)
    numCourses = 2
    prerequisites = [[1,0],[0,1]]
    print("Test Case 2 Output:", sol.findOrder(numCourses, prerequisites))
    # Expected: []

    # Test Case 3
    numCourses = 1
    prerequisites = []
    print("Test Case 3 Output:", sol.findOrder(numCourses, prerequisites))
    # Expected: [0]
