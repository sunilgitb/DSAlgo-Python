# https://leetcode.com/problems/rectangle-overlap/

from typing import List

class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        x1, y1, x2, y2 = rec1
        x3, y3, x4, y4 = rec2
        
        # check y intersection
        if y4 <= y1 or y2 <= y3:
            return False
        
        # check x intersection
        if x1 >= x4 or x2 <= x3:
            return False
        
        return True


# ----------------- Driver Code -----------------
sol = Solution()

rectangles = [
    ([0,0,2,2], [1,1,3,3]),
    ([0,0,1,1], [1,0,2,1]),
    ([0,0,1,1], [2,2,3,3])
]

for rec1, rec2 in rectangles:
    print(f"Rectangles {rec1} & {rec2} overlap? {sol.isRectangleOverlap(rec1, rec2)}")

# Time: O(1)
# Space: O(1)
