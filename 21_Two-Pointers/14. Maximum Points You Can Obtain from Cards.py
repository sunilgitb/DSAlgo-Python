# https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/

from typing import List

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        total = sum(cardPoints)

        # window size to remove
        window = n - k
        if window == 0:
            return total

        curr_sum = sum(cardPoints[:window])
        min_sum = curr_sum

        for i in range(window, n):
            curr_sum += cardPoints[i]
            curr_sum -= cardPoints[i - window]
            min_sum = min(min_sum, curr_sum)

        return total - min_sum


if __name__ == "__main__":
    solution = Solution()

    cardPoints = [1,2,3,4,5,6,1]
    k = 3
    print(solution.maxScore(cardPoints, k))
    # Output: 12
    # Explanation: Pick 6,5,1

    cardPoints = [2,2,2]
    k = 2
    print(solution.maxScore(cardPoints, k))
    # Output: 4

    cardPoints = [9,7,7,9,7,7,9]
    k = 7
    print(solution.maxScore(cardPoints, k))
    # Output: 55
