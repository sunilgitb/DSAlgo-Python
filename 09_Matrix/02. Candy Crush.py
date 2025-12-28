# https://www.lintcode.com/problem/858/
# https://leetcode.com/problems/candy-crush/
# Explanation: https://algo.monster/liteproblems/723

from typing import List

class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        # Dimensions of the board
        num_rows, num_cols = len(board), len(board[0])
      
        # Flag to indicate if we should continue crushing candies
        should_crush = True
      
        # Keep crushing candies until no more moves can be made
        while should_crush:
            should_crush = False  # Reset the flag for each iteration
          
            # Mark the candies to be crushed horizontally
            for row in range(num_rows):
                for col in range(num_cols - 2):
                    candy_value = abs(board[row][col])
                    # Check if three consecutive candies have the same value
                    if candy_value != 0 and candy_value == abs(board[row][col + 1]) == abs(board[row][col + 2]):
                        should_crush = True  # We will need another pass after crushing
                        # Mark the candies for crushing by negating their value
                        board[row][col] = board[row][col + 1] = board[row][col + 2] = -candy_value
                      
            # Mark the candies to be crushed vertically
            for col in range(num_cols):
                for row in range(num_rows - 2):
                    candy_value = abs(board[row][col])
                    # Check if three consecutive candies vertically have the same value
                    if candy_value != 0 and candy_value == abs(board[row + 1][col]) == abs(board[row + 2][col]):
                        should_crush = True  # We will need another pass after crushing
                        # Mark the candies for crushing
                        board[row][col] = board[row + 1][col] = board[row + 2][col] = -candy_value
                      
            # Drop the candies to fill the empty spaces caused by crushing
            if should_crush:
                for col in range(num_cols):
                    # Pointer to where the next non-crushed candy will fall
                    write_row = num_rows - 1
                    for row in range(num_rows - 1, -1, -1):
                        # If the candy is not marked for crushing, bring it down
                        if board[row][col] > 0:
                            board[write_row][col] = board[row][col]
                            write_row -= 1
                    # Fill the remaining spaces at the top with zeros
                    while write_row >= 0:
                        board[write_row][col] = 0
                        write_row -= 1
                      
        # Return the modified board after all possible crushes are completed
        return board


# Time: O((m * n) * (m * n)) or O((m * n)^2)
# Space: O(1)
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
