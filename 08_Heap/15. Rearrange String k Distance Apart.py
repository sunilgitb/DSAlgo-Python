# https://www.lintcode.com/problem/907

import heapq
import collections

class Solution:
    def rearrangeString(self, s, k):
        maxHeap = []
        heapq.heapify(maxHeap)
        for (ch, cnt) in collections.Counter(s).items():
            heapq.heappush(maxHeap, (-cnt, ch))

        res = ""
        while len(maxHeap) >= k:
            tmp = []
            for _ in range(k):
                cnt, ch = heapq.heappop(maxHeap)
                res += ch
                tmp.append((cnt, ch))
            for cnt, ch in tmp:
                cnt += 1
                if cnt < 0:
                    heapq.heappush(maxHeap, (cnt, ch))
        
        if len(maxHeap) > 0:
            cnt, ch = heapq.heappop(maxHeap)
            if cnt < -1: return ""
            res += ch
        
        return res 


# Time: O(len(s) * log n), where len(s) is the length of the input string and n is the number of distinct characters.
# Space: O(len(s))
if __name__ == "__main__":
    sol = Solution()

    # Test Case 1
    s = "aabbcc"
    k = 3
    print("Rearranged string:", sol.rearrangeString(s, k))
    # Possible output: "abcabc"
    # Explanation: No two same characters are within distance 3.

    # Test Case 2
    s = "aaabc"
    k = 3
    print("Rearranged string:", sol.rearrangeString(s, k))
    # Expected output: "" (Not possible)
    # Explanation: Cannot rearrange 'a' to satisfy distance 3.

    # Test Case 3
    s = "aaadbbcc"
    k = 2
    print("Rearranged string:", sol.rearrangeString(s, k))
    # Possible output: "abacabcd"
    # Explanation: Each same character is at least distance 2 apart.
