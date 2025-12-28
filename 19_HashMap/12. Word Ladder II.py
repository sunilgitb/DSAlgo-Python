# https://leetcode.com/problems/word-ladder-ii/

from typing import List
import collections

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        wordList = set(wordList)  # O(1) lookups
        if beginWord == endWord:
            return [[beginWord]]  # trivial case

        q = collections.deque([[beginWord, []]])
        res = []

        while q:
            word, path = q.popleft()
            if word in wordList:
                wordList.remove(word)  # prevent revisiting

            if word == endWord:
                if not res or len(path) + 1 == len(res[0]):
                    res.append(path + [word])
                elif len(path) + 1 > len(res[0]):
                    break  # all further paths will be longer
            else:
                for i in range(len(word)):
                    for letter in alphabet:
                        next_word = word[:i] + letter + word[i+1:]
                        if next_word in wordList:
                            q.append([next_word, path + [word]])
        return res

# ================= DRIVER CODE =================
if __name__ == "__main__":
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log","cog"]

    sol = Solution()
    ladders = sol.findLadders(beginWord, endWord, wordList)
    print("All shortest transformation sequences:")
    for seq in ladders:
        print(seq)

