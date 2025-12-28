# https://leetcode.com/problems/longest-substring-without-repeating-characters/

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


# -------- Driver Code --------
solution = Solution()

print(solution.lengthOfLongestSubstring("abcabcbb"))  # 3
print(solution.lengthOfLongestSubstring("bbbbb"))     # 1
print(solution.lengthOfLongestSubstring("pwwkew"))    # 3
print(solution.lengthOfLongestSubstring(""))           # 0
print(solution.lengthOfLongestSubstring("dvdf"))       # 3
