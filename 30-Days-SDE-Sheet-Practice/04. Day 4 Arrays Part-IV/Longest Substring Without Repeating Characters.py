# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# https://youtu.be/qtVh-XEpsJo

# https://leetcode.com/problems/longest-substring-without-repeating-characters/

'''
Sliding Window + HashSet

- Use two pointers (l, r)
- Expand right pointer
- If duplicate found, shrink from left
- Track maximum window size
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        track = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in track:
                track.remove(s[l])
                l += 1

            track.add(s[r])
            res = max(res, r - l + 1)

        return res


# ---------------- DRIVER CODE ----------------
if __name__ == "__main__":
    sol = Solution()

    s = "abcabcbb"

    print("Input String:", s)
    print("Length of Longest Substring Without Repeating Characters:",
          sol.lengthOfLongestSubstring(s))

# Time Complexity: O(N)   
# Space Complexity: O(len(set(s)))  # number of unique charecters

