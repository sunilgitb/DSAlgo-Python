# https://leetcode.com/problems/longest-consecutive-sequence/

'''
Idea:
- Put all elements into a set for O(1) lookup
- Start counting only from numbers whose (num - 1) does NOT exist
- Extend forward to count consecutive numbers
'''

class Solution:
    def longestConsecutive(self, nums):
        if not nums:
            return 0

        track = set(nums)
        res = 0

        for num in nums:
            # start only if it's the beginning of a sequence
            if (num - 1) not in track:
                curr = num
                length = 1

                while (curr + 1) in track:
                    curr += 1
                    length += 1

                res = max(res, length)

        return res


# ---------------- DRIVER CODE ----------------
if __name__ == "__main__":
    sol = Solution()

    nums = [100, 4, 200, 1, 3, 2]

    print("Array:", nums)
    print("Longest Consecutive Sequence Length:", sol.longestConsecutive(nums))
