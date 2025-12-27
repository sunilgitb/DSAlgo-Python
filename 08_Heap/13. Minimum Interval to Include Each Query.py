# https://leetcode.com/problems/minimum-interval-to-include-each-query/
# https://youtu.be/5hQ5WWW5awQ

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        minHeap, i = [], 0 
        res = {} # Dictionary to retrive values as order of queries
        
        for q in sorted(queries):
            while i < len(intervals) and intervals[i][0] <= q:
                l, r = intervals[i]
                heapq.heappush(minHeap, (r-l+1, r))
                i += 1
                
            while minHeap and minHeap[0][1] < q:
                heapq.heappop(minHeap)
                
            res[q] = minHeap[0][0] if minHeap else -1
                
        return [res[q] for q in queries]
    
    
    
# Time: O(N log(N) + Qlog(Q))
if __name__ == "__main__":
    sol = Solution()

    # Test Case 1
    intervals = [[1,4],[2,4],[3,6]]
    queries = [2,3,4,5]
    print("Minimum intervals:", sol.minInterval(intervals, queries))
    # Expected Output: [3,3,3,4]
    # Explanation:
    # Query 2 → interval [2,4] or [1,4], smallest length = 3
    # Query 3 → interval [3,6] or [2,4] or [1,4], smallest length = 3
    # Query 4 → same as above, smallest length = 3
    # Query 5 → interval [3,6], length = 4

    # Test Case 2
    intervals = [[2,3],[2,5],[1,8],[20,25]]
    queries = [2,19,5,22]
    print("Minimum intervals:", sol.minInterval(intervals, queries))
    # Expected Output: [2,-1,4,6]
