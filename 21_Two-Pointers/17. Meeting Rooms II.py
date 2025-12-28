# https://www.lintcode.com/problem/919
# https://leetcode.com/problems/meeting-rooms-ii/
# https://www.youtube.com/watch?v=FdzJmTCVyJU


from typing import List

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        
        start = sorted(i[0] for i in intervals)
        end = sorted(i[1] for i in intervals)
        
        s = e = 0
        res = 0
        
        while s < len(intervals):
            if start[s] < end[e]:
                s += 1
            else:
                e += 1
            res = max(res, s - e)
        
        return res


# ---------------- DRIVER CODE ----------------
if __name__ == "__main__":
    solution = Solution()

    intervals1 = [[0, 30], [5, 10], [15, 20]]
    print(solution.minMeetingRooms(intervals1))
    # Output: 2

    intervals2 = [[7, 10], [2, 4]]
    print(solution.minMeetingRooms(intervals2))
    # Output: 1

    intervals3 = [[1, 5], [2, 6], [3, 7], [4, 8]]
    print(solution.minMeetingRooms(intervals3))
    # Output: 4


# Time: O(N log N)
# Space: O(N)
