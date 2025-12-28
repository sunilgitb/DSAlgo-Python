# https://leetcode.com/problems/word-ladder/
# https://youtu.be/ZVJ3asMoZ18

from typing import List
import collections

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList or not endWord or not beginWord or not wordList: 
            return 0
        wordList.append(beginWord)
        dct = {}
        for word in wordList:
            for i in range(len(word)):
                cur = word[:i] + '*' + word[i+1:]
                if cur not in dct:
                    dct[cur] = [word]
                else:
                    dct[cur].append(word)
        
        q = collections.deque()
        visited = {beginWord}
        q.append((beginWord, 1))
        while q:
            cur, level = q.popleft()
            for i in range(len(cur)):
                key = cur[:i] + '*' + cur[i+1:]
                for word in dct[key]:
                    if word == endWord: 
                        return level + 1
                    if word not in visited:
                        q.append((word, level+1))
                        visited.add(word)
        return 0

# ================= DRIVER CODE =================
if __name__ == "__main__":
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log","cog"]
    
    sol = Solution()
    length = sol.ladderLength(beginWord, endWord, wordList)
    print(f"Length of shortest transformation sequence: {length}")

    
# Time: O(N * M^2)  # N = len(beginWord); M = len(wordList)
