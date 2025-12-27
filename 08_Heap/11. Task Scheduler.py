# https://leetcode.com/problems/task-scheduler/
# https://youtu.be/s8p8ukTyA2I

class Solution:
    def leastInterval(self, tasks, n):
        taskCnt = collections.Counter(tasks)
        maxHeap = [-cnt for cnt in taskCnt.values()]
        heapq.heapify(maxHeap)
        
        time = 0
        q = collections.deque()
        while maxHeap or q:
            time += 1
            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append((cnt, time + n))
            if q and time == q[0][1]:
                heapq.heappush(maxHeap, q.popleft()[0])
        
        return time
    
    
# Time: O(len(tasks) * n)
if __name__ == "__main__":
    sol = Solution()
    
    # Test Case 1
    tasks = ["A","A","A","B","B","B"]
    n = 2
    print("Minimum intervals:", sol.leastInterval(tasks, n))
    # Expected Output: 8
    # Explanation: One possible schedule is A -> B -> idle -> A -> B -> idle -> A -> B

    # Test Case 2
    tasks = ["A","A","A","B","B","B"]
    n = 0
    print("Minimum intervals:", sol.leastInterval(tasks, n))
    # Expected Output: 6
    # Explanation: No cooldown, so schedule as A B A B A B

    # Test Case 3
    tasks = ["A","A","A","B","B","B","C","C"]
    n = 2
    print("Minimum intervals:", sol.leastInterval(tasks, n))
    # Expected Output: 8
    # Explanation: Schedule example: A B C A B C A B
