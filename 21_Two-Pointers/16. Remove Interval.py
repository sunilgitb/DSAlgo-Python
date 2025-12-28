# https://www.lintcode.com/problem/3678
# https://leetcode.com/problems/remove-interval/description/

from typing import List

class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        ans = []

        for a, b in intervals:
            # Case 1: No overlap
            if b <= toBeRemoved[0] or a >= toBeRemoved[1]:
                ans.append([a, b])
            else:
                # Case 2: Partial overlap on left
                if a < toBeRemoved[0]:
                    ans.append([a, toBeRemoved[0]])

                # Case 3: Partial overlap on right
                if b > toBeRemoved[1]:
                    ans.append([toBeRemoved[1], b])

        return ans


if __name__ == "__main__":
    solution = Solution()

    intervals = [[0,2],[3,4],[5,7]]
    toBeRemoved = [1,6]
    print(solution.removeInterval(intervals, toBeRemoved))
    # Output: [[0,1],[6,7]]

    intervals = [[0,5]]
    toBeRemoved = [2,3]
    print(solution.removeInterval(intervals, toBeRemoved))
    # Output: [[0,2],[3,5]]

    intervals = [[0,5]]
    toBeRemoved = [0,5]
    print(solution.removeInterval(intervals, toBeRemoved))
    # Output: []

    intervals = [[-5,-4],[-3,-2],[1,2]]
    toBeRemoved = [-3,1]
    print(solution.removeInterval(intervals, toBeRemoved))
    # Output: [[-5,-4],[1,2]]


# Time: O(n)
# Space: O(n)
