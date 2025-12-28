# https://leetcode.com/problems/minimum-number-of-flips-to-make-the-binary-string-alternating/
# https://youtu.be/MOeuK6gaC2A

class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        s = s + s  # simulate rotation
        
        alt1 = []  # "010101..."
        alt2 = []  # "101010..."
        
        for i in range(len(s)):
            alt1.append('0' if i % 2 == 0 else '1')
            alt2.append('1' if i % 2 == 0 else '0')
        
        diff1 = diff2 = 0
        
        # initial window
        for i in range(n):
            if s[i] != alt1[i]:
                diff1 += 1
            if s[i] != alt2[i]:
                diff2 += 1
        
        res = min(diff1, diff2)
        l = 0
        
        # sliding window
        for r in range(n, len(s)):
            if s[r] != alt1[r]:
                diff1 += 1
            if s[r] != alt2[r]:
                diff2 += 1
            
            if s[l] != alt1[l]:
                diff1 -= 1
            if s[l] != alt2[l]:
                diff2 -= 1
            
            l += 1
            res = min(res, diff1, diff2)
        
        return res


if __name__ == "__main__":
    solution = Solution()
    
    s = "111000"
    print(solution.minFlips(s))
    # Output: 2
    # Explanation: Rotate and flip to "010101"
    
    s = "010"
    print(solution.minFlips(s))
    # Output: 0
    # Already alternating
    
    s = "1110"
    print(solution.minFlips(s))
    # Output: 1

    
    
# Time: O(N)
# Space: O(1)
