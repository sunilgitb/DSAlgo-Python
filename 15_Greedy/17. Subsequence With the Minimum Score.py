class Solution:
    def minimumScore(self, s: str, t: str) -> int:
        n, m = len(s), len(t)
        
        # If t is already a subsequence of s, we can remove 0 characters
        j = 0
        for char in s:
            if j < m and char == t[j]:
                j += 1
        if j == m:
            return 0
        
        # left[i] = number of characters from t matched using first i+1 characters of s
        left = [0] * n
        j = 0
        for i in range(n):
            if j < m and s[i] == t[j]:
                j += 1
            left[i] = j
        
        # right[i] = number of characters from t matched using last i+1 characters of s (from right)
        right = [0] * n
        j = m - 1
        for i in range(n - 1, -1, -1):
            if j >= 0 and s[i] == t[j]:
                j -= 1
            right[i] = m - 1 - j  # count matched from the end
        
        # Minimum number of removals = m - maximum number of matches we can keep
        min_removals = m
        
        # Try every possible split point i in s
        # Left part matches left[i] characters of t
        # Right part matches right[i+1] characters of t
        # Total matched = left[i] + right[i+1]
        # Removals = m - total matched
        for i in range(n - 1):
            total_matched = left[i] + right[i + 1]
            min_removals = min(min_removals, m - total_matched)
        
        # Also consider using only left part or only right part
        min_removals = min(min_removals, m - left[-1])
        min_removals = min(min_removals, m - right[0])
        
        return min_removals

def test():
    sol = Solution()
    assert sol.minimumScore("abacaba", "bzaa") == 1
    assert sol.minimumScore("abc", "abc") == 0
    assert sol.minimumScore("a", "b") == 1
    assert sol.minimumScore("abcd", "abcde") == 1
    assert sol.minimumScore("xyz", "xyz") == 0
    print("All tests passed!")

test()