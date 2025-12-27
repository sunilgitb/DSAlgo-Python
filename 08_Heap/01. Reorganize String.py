# https://leetcode.com/problems/reorganize-string/

import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = {}
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1
        
        maxHeap = []
        for ch in freq:
            heapq.heappush(maxHeap, [-freq[ch], ch])
        
        ans = ""
        
        while len(maxHeap) > 1:
            cnt1, ch1 = heapq.heappop(maxHeap)
            cnt2, ch2 = heapq.heappop(maxHeap)
            
            ans += ch1
            ans += ch2
            
            if cnt1 < -1:
                heapq.heappush(maxHeap, [cnt1 + 1, ch1])
            if cnt2 < -1:
                heapq.heappush(maxHeap, [cnt2 + 1, ch2])
        
        if maxHeap:
            cnt, ch = heapq.heappop(maxHeap)
            if cnt < -1:
                return ""
            ans += ch
        
        return ans


# ---------------- DRIVER CODE ----------------
if __name__ == "__main__":
    sol = Solution()
    
    s1 = "aab"
    print(sol.reorganizeString(s1))
    # Output: "aba"
    
    s2 = "aaab"
    print(sol.reorganizeString(s2))
    # Output: ""
    
    s3 = "vvvlo"
    print(sol.reorganizeString(s3))
    # Output: "vlvov" (one valid output)
