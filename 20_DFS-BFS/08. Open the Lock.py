# https://leetcode.com/problems/open-the-lock/
# https://youtu.be/Pzg3bCDY87w

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        if '0000' in deadends: 
            return -1
        
        def children(lock):
            arr = []
            for i in range(4):
                cur = int(lock[i])
                arr.append(lock[:i] + str((cur+1)%10) + lock[i+1:])
                arr.append(lock[:i] + str((cur-1)%10) + lock[i+1:])
            return arr
            
        visited = set()
        q = collections.deque()
        q.append(['0000', 0])
            
        while q:
            lock, turns = q.popleft()
            if lock == target: 
                return turns
            for child in children(lock):
                if child not in deadends and child not in visited:
                    visited.add(child)
                    q.append([child, turns+1])
        
        return -1
                    
            
if __name__ == "__main__":
    solution = Solution()
    
    deadends = ["0201","0101","0102","1212","2002"]
    target = "0202"
    print(solution.openLock(deadends, target))  # Output: 6

    deadends = ["8888"]
    target = "0009"
    print(solution.openLock(deadends, target))  # Output: 1

    deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"]
    target = "8888"
    print(solution.openLock(deadends, target))  # Output: -1
