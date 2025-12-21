# https://leetcode.com/problems/merge-intervals/
# sort based on the 0th index element value
# check values of two consecutive elements with 2 pointers. if overlapping then change 1st index of 
# 1st pointer with max and pop 2nd pointer
from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x : x[0])
        l = 0
        r = 1
        
        while r < len(intervals):
            if intervals[l][1] >= intervals[r][0]:
                intervals[l][1] = max(intervals[l][1], intervals[r][1])
                intervals.pop(r)
            else:
                l = r
                r += 1
        
        return intervals

# Hardcoded intervals
intervals = [[1,3],[2,6],[8,10],[15,18]]

sol = Solution()
merged_intervals = sol.merge(intervals)
print("Merged Intervals:", merged_intervals)
# Merged Intervals: [[1, 6], [8, 10], [15, 18]]
