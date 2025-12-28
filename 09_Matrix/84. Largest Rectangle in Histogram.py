from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Finding Left Boundary
        stack = []
        lb = []  # Left Boundary
        
        for i in range(len(heights)):
            while stack:
                if heights[stack[-1]] >= heights[i]:
                    stack.pop()
                else:
                    lb.append(stack[-1] + 1)
                    stack.append(i)
                    break
            if not stack:
                stack.append(i)
                lb.append(0)

        # Finding Right Boundary
        stack = []
        rb = []
        
        for i in range(len(heights) - 1, -1, -1):
            while stack:
                if heights[stack[-1]] >= heights[i]:
                    stack.pop()
                else:
                    rb.append(stack[-1] - 1)
                    stack.append(i)
                    break
            if not stack:
                stack.append(i)
                rb.append(len(heights) - 1)

        rb.reverse()

        # Calculate max area
        maxArea = 0
        for i in range(len(heights)):
            width = rb[i] - lb[i] + 1
            maxArea = max(maxArea, width * heights[i])

        return maxArea


# ---------------- DRIVER CODE ----------------
if __name__ == "__main__":
    sol = Solution()

    heights = [2, 1, 5, 6, 2, 3]
    print("Histogram:", heights)

    result = sol.largestRectangleArea(heights)
    print("Largest Rectangle Area:", result)
