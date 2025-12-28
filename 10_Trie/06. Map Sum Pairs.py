# https://leetcode.com/problems/map-sum-pairs/

class TrieNode:
    def __init__(self):
        self.children = {}
        self.prefixCount = 0


class MapSum:
    def __init__(self):
        self.root = TrieNode()
        self.dic = {}   # to store existing key-value pairs

    def insert(self, key: str, val: int) -> None:
        # calculate delta to handle overwrite
        delta = val - self.dic.get(key, 0)
        self.dic[key] = val

        cur = self.root
        for c in key:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
            cur.prefixCount += delta

    def sum(self, prefix: str) -> int:
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return 0
            cur = cur.children[c]
        return cur.prefixCount


# ---------------- DRIVER CODE ----------------

ms = MapSum()

ms.insert("apple", 3)
print(ms.sum("ap"))     # Expected: 3

ms.insert("app", 2)
print(ms.sum("ap"))     # Expected: 5

ms.insert("apple", 2)   # overwrite apple from 3 → 2
print(ms.sum("ap"))     # Expected: 4
