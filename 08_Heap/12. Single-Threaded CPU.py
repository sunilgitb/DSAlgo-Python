# https://leetcode.com/problems/single-threaded-cpu/
# https://youtu.be/RR1n-d4oYqE

import heapq
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i,t in enumerate(tasks):
            t.append(i)
        tasks.sort(key = lambda x:x[0])
        
        res, minHeap = [], []
        i, time = 0, tasks[0][0]
        
        while i < len(tasks) or minHeap:
            while i < len(tasks) and time >= tasks[i][0] :
                heapq.heappush(minHeap, (tasks[i][1], tasks[i][2]))
                i += 1
            if not minHeap:
                time = tasks[i][0]
            else:
                procTime, indx = heapq.heappop(minHeap)
                res.append(indx)
                time += procTime
        
        return res
    
    
# Time: O(N)
# Space: O(N)
if __name__ == "__main__":
    sol = Solution()

    # Test Case 1
    tasks = [[1,2],[2,4],[3,2],[4,1]]
    print("Order of processing:", sol.getOrder(tasks))
    # Expected Output: [0,2,3,1]
    # Explanation: 
    # Time 1: Task 0 arrives, executed
    # Time 3: Tasks 1 and 2 available, pick task 2 (shortest processing time)
    # Time 5: Task 3 available, pick task 3
    # Time 6: Pick remaining task 1

    # Test Case 2
    tasks = [[7,10],[7,12],[7,5],[7,4],[7,2]]
    print("Order of processing:", sol.getOrder(tasks))
    # Expected Output: [4,3,2,0,1]
    # Explanation: All arrive at same time, process by shortest processing time and index
