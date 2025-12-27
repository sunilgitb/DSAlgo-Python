# Mock Celebrity API
class Celebrity:
    matrix = []

    @staticmethod
    def knows(a, b):
        return Celebrity.matrix[a][b]


class Solution:
    def findCelebrity(self, n):
        celeb = 0

        # Step 1: Find potential celebrity
        for i in range(1, n):
            if Celebrity.knows(celeb, i):
                celeb = i

        # Step 2: Verify candidate
        for i in range(n):
            if i != celeb:
                if Celebrity.knows(celeb, i) or not Celebrity.knows(i, celeb):
                    return -1

        return celeb


# ---------------- DRIVER CODE ----------------

if __name__ == "__main__":
    # Example:
    # Person 2 is celebrity
    Celebrity.matrix = [
        [False, True,  True,  False],
        [False, False, True,  False],
        [False, False, False, False],  # Celebrity: knows no one
        [False, True,  True,  False]
    ]

    n = len(Celebrity.matrix)

    sol = Solution()
    result = sol.findCelebrity(n)

    print("Celebrity Index:", result)
    # Expected Output: Celebrity Index: 2
