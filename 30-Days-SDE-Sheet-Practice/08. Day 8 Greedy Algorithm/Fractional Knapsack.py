# https://leetcode.com/problems/maximum-units-on-a-truck/
'''
As we need to find maximum units, sort the boxTypes in decreasing order
of units per box. Then greedily take as many boxes as possible.
'''

from typing import List

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        res = 0

        for boxes, units in boxTypes:
            if truckSize >= boxes:
                res += boxes * units
                truckSize -= boxes
            else:
                res += truckSize * units
                break

        return res


# ---------------- DRIVER CODE ----------------
if __name__ == "__main__":
    sol = Solution()

    boxTypes = [[1,3],[2,2],[3,1]]
    truckSize = 4
    print(sol.maximumUnits(boxTypes, truckSize))
    # Expected Output: 8

    boxTypes = [[5,10],[2,5],[4,7],[3,9]]
    truckSize = 10
    print(sol.maximumUnits(boxTypes, truckSize))
    # Expected Output: 91

    boxTypes = [[1,3],[5,5],[2,10]]
    truckSize = 3
    print(sol.maximumUnits(boxTypes, truckSize))
    # Expected Output: 23
