# https://leetcode.com/problems/the-skyline-problem/
# https://youtu.be/POUMNJou4vc

import heapq
class Solution:
    def getSkyline(self, buildings):
        corners = []
        for l, r, h in buildings:
            corners.append((l, -h))
            corners.append((r, h))
        corners.sort()
        print(corners)
        # as heapq does not support delete element by value. 
        removed = collections.Counter()
        maxHeap = [0]
        res = []
        
        def getMaxHeight():
            mh = - maxHeap[0]  # max height
            while mh in removed:
                removed[mh] -= 1
                if removed[mh] == 0: del removed[mh]
                heapq.heappop(maxHeap)
                mh = - maxHeap[0]
            return mh
        
        for x, y in corners:
            mh = getMaxHeight()
            if y < 0:
                if -y > mh:
                    res.append([x, -y])
                heapq.heappush(maxHeap, y)
            else:
                ph = mh
                removed[y] += 1
                if y == mh:
                    mh = getMaxHeight()
                    if ph > mh: res.append([x, mh])
        
        return res
    
    
# Time: O(N log(N))
# Space: O(N)
if __name__ == "__main__":
    sol = Solution()

    # Test Case 1
    buildings = [[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]
    print("Skyline:", sol.getSkyline(buildings))
    # Expected Output: [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]

    # Test Case 2
    buildings = [[0, 2, 3], [2, 5, 3]]
    print("Skyline:", sol.getSkyline(buildings))
    # Expected Output: [[0,3],[5,0]]

    # Test Case 3
    buildings = [[1, 3, 4], [2, 4, 4], [5, 6, 1]]
    print("Skyline:", sol.getSkyline(buildings))
    # Expected Output: [[1,4],[4,0],[5,1],[6,0]]
