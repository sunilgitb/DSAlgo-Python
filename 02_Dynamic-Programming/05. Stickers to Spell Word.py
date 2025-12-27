from typing import List
from collections import Counter

class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        target_set = set(target)
        stick_counts = []
        
        for sticker in stickers:
            stick = {}
            for ch in sticker:
                if ch in target_set:
                    stick[ch] = stick.get(ch, 0) + 1
            if stick:  # Only add stickers that have relevant characters
                stick_counts.append(stick)
        
        dp = {}
        
        def dfs(t):
            if not t:
                return 0
            if t in dp:
                return dp[t]
            
            res = float('inf')
            t_counter = Counter(t)
            
            for stick in stick_counts:
                # Optimization: Only use stickers that contain the first character of t
                if t[0] not in stick:
                    continue
                    
                # Apply the sticker
                new_t = []
                for ch, count in t_counter.items():
                    remaining = count - stick.get(ch, 0)
                    if remaining > 0:
                        new_t.extend([ch] * remaining)
                
                # Create new target string
                new_target = ''.join(sorted(new_t))
                next_res = dfs(new_target)
                if next_res != -1:
                    res = min(res, 1 + next_res)
            
            dp[t] = res if res != float('inf') else -1
            return dp[t]
        
        # Sort target to normalize state representation
        sorted_target = ''.join(sorted(target))
        return dfs(sorted_target)


# Test cases
solution = Solution()

# Test 1
stickers1 = ["with", "example", "science"]
target1 = "thehat"
print("Test 1:", solution.minStickers(stickers1, target1))  # Expected: 3

# Test 2
stickers2 = ["notice", "possible"]
target2 = "basicbasic"
print("Test 2:", solution.minStickers(stickers2, target2))  # Expected: -1

# Test 3
stickers3 = ["these", "guess", "about", "garden", "him"]
target3 = "atomher"
print("Test 3:", solution.minStickers(stickers3, target3))  # Expected: 3

# Test 4
stickers4 = ["ab", "bc", "ac"]
target4 = "abc"
print("Test 4:", solution.minStickers(stickers4, target4))  # Expected: 2