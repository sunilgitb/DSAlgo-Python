# https://leetcode.com/problems/jump-game-vii/
# https://youtu.be/v1HpZUnQ4Yo

class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        q = deque([0])
        furthest = 0
        
        while q:
            i = q.popleft()
            start = max(i+minJump, furthest+1)
            for j in range(start, min(i+maxJump+1, len(s))):
                if s[j] == '0':
                    if j == len(s)-1:
                        return True
                    q.append(j)
            furthest = i+maxJump
            
        return False
                
if __name__ == "__main__":
    solution = Solution()
    
    s = "011010"
    minJump = 2
    maxJump = 3
    print(solution.canReach(s, minJump, maxJump))  # Output: True
    # Explanation: Jump from 0 -> 3 -> 5

    s = "01101110"
    minJump = 2
    maxJump = 3
    print(solution.canReach(s, minJump, maxJump))  # Output: False
    # Explanation: Cannot reach the last index

        
# Time: O(N)
# as due to the furthest we are not appending nested indices in q
