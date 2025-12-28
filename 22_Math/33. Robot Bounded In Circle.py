# https://leetcode.com/problems/robot-bounded-in-circle/


# https://leetcode.com/problems/robot-bounded-in-circle/
# Robot Bounded In Circle
# Problem: Given instructions for a robot ('G' = move forward, 'L' = turn left 90°, 'R' = turn right 90°),
# return true if after some number of repetitions the robot is bounded in a circle (never goes infinitely far).

class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        """
        Optimal O(n) solution:
        - Simulate movement for up to 4 repetitions (cycle of directions is 4)
        - Robot is bounded if after 1, 2, or 4 repetitions it returns to origin OR
          faces a different direction (will cycle in a loop)
        - Key insight: After 4 instructions, robot must face north again if it repeats forever
        """
        x, y = 0, 0
        dx, dy = 0, 1  # initial direction: north
        
        # Simulate up to 4 repetitions (full cycle)
        for _ in range(4):
            for move in instructions:
                if move == 'G':
                    x += dx
                    y += dy
                elif move == 'L':
                    dx, dy = -dy, dx   # left turn: (dx, dy) -> (-dy, dx)
                elif move == 'R':
                    dx, dy = dy, -dx   # right turn: (dx, dy) -> (dy, -dx)
        
        # Robot is bounded if it returned to origin after 4 cycles
        return (x == 0 and y == 0)


# Driver Code with test cases
if __name__ == "__main__":
    solution = Solution()
    
    test_cases = [
        ("GGLLGG", True),      # returns to origin
        ("GG", False),         # goes infinitely far
        ("GL", True),          # cycles in a square
        ("GLR", True),         # small loop
        ("LLL", True),         # turns 270° left (equivalent to right)
        ("", True),            # empty instructions → stays at origin
        ("GGGG", False),       # goes straight forever
        ("GRL", True),         # small loop
    ]
    
    print("Testing Robot Bounded In Circle\n" + "="*50)
    
    for idx, (instructions, expected) in enumerate(test_cases, 1):
        result = solution.isRobotBounded(instructions)
        status = "✓ PASS" if result == expected else "✗ FAIL"
        print(f"Test {idx:2d}: {status}")
        print(f"   Instructions: '{instructions}'")
        print(f"   Output:       {result} (Expected: {expected})")
        print("-" * 50)
# Time: O(N)
# Space: O(1)
