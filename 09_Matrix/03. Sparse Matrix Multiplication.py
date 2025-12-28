# https://www.lintcode.com/problem/654/
# https://leetcode.com/problems/sparse-matrix-multiplication/

class Solution:
    def multiply(self, a: List[List[int]], b: List[List[int]]) -> List[List[int]]:
        aRow, aCol, bRow, bCol = len(a), len(a[0]), len(b), len(b[0])
        res = [[0]*bCol for _ in range(aRow)]
        for i in range(aRow):
            for j in range(bCol):
                for k in range(bRow):
                    res[i][j] += a[i][k] * b[k][j]
        return res 

# Time: O(aRow * bCol * bRow)
# Space: O(aRow * bCol)

if __name__ == "__main__":
    sol = Solution()

    # Example 1 (LeetCode official example)
    board = [
        [110, 5, 112, 113, 114],
        [210, 211, 5, 213, 214],
        [310, 311, 3, 313, 314],
        [410, 411, 412, 5, 414],
        [5,   1,   512, 3,   3],
        [610, 4,   1,   613, 614],
        [710, 1,   2,   713, 714],
        [810, 1,   2,   1,   1],
        [1,   1,   2,   2,   2],
        [4,   1,   4,   4,   1014]
    ]

    print("Original Board:")
    for row in board:
        print(row)

    result = sol.candyCrush(board)

    print("\nFinal Board After Candy Crush:")
    for row in result:
        print(row)
