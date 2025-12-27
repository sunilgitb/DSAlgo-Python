class Solution:
    def candy(self, ratings):
        n = len(ratings)
        candies = [1] * n  # everyone gets at least 1 candy

        # Left to right: ensure right neighbor gets more if rating increases
        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                candies[i] = candies[i-1] + 1

        # Right to left: ensure left neighbor gets more if rating increases
        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                candies[i] = max(candies[i], candies[i+1] + 1)

        return sum(candies)

# ------------------- Driver Code -------------------
if __name__ == "__main__":
    sol = Solution()
    ratings = [1, 0, 2]
    print(sol.candy(ratings))  # Output: 5
