# https://leetcode.com/problems/insert-delete-getrandom-o1/

class RandomizedSet:

    def __init__(self):
        self.val2ind = {}
        self.arr = []

    def insert(self, val: int) -> bool:
        if val in self.val2ind: 
            return False
        self.val2ind[val] = len(self.arr)
        self.arr.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.val2ind: 
            return False
        last = self.arr[-1]
        ind = self.val2ind[val]
        self.val2ind[last] = ind
        self.arr[ind] = last
        self.arr.pop()
        del self.val2ind[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.arr)

if __name__ == "__main__":
    obj = RandomizedSet()
    
    print(obj.insert(1))   # True, inserted
    print(obj.insert(2))   # True, inserted
    print(obj.insert(1))   # False, already exists
    
    print(obj.getRandom()) # Randomly 1 or 2
    
    print(obj.remove(1))   # True, removed
    print(obj.remove(3))   # False, does not exist
    
    print(obj.getRandom()) # Should return 2 as 1 is removed
