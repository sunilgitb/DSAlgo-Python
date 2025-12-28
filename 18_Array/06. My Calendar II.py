# https://leetcode.com/problems/my-calendar-ii/
# https://youtu.be/_7B_HzJUE6E

'''
class MyCalendarTwo:
    
    def __init__(self):
        self.dct = {}
    
    def book(self, start: int, end: int) -> bool:
        self.dct[start] = self.dct[start] + 1 if start in self.dct else 1
        self.dct[end] = self.dct[end] - 1 if end in self.dct else -1
        
        arr = sorted(self.dct.keys())
        s = 0
        for i in arr:
            s += self.dct[i]
            if s >= 3:
                self.dct[start] -= 1
                self.dct[end] += 1
                return False
            
        return True
        
        
# Time: O(N log(N))
# Space: O(N)
'''



# https://leetcode.com/problems/my-calendar-ii/
# https://youtu.be/_7B_HzJUE6E

class MyCalendarTwo:

    def __init__(self):
        self.calendar = []   # stores all single bookings
        self.overlaps = []   # stores double-booked intervals

    def book(self, start: int, end: int) -> bool:
        # If it overlaps with any double booking → triple booking → reject
        for s, e in self.overlaps:
            if s < end and start < e:
                return False
        
        # Check overlaps with existing bookings
        for s, e in self.calendar:
            if s < end and start < e:
                # record the overlapping interval
                self.overlaps.append([max(s, start), min(e, end)])
        
        # Add current booking
        self.calendar.append([start, end])
        return True


# ---------------- DRIVER CODE ----------------
if __name__ == "__main__":
    cal = MyCalendarTwo()

    print(cal.book(10, 20))  # True
    print(cal.book(50, 60))  # True
    print(cal.book(10, 40))  # True (double booking allowed)
    print(cal.book(5, 15))   # False (would cause triple booking)
    print(cal.book(5, 10))   # True
    print(cal.book(25, 55))  # True



# Time: O(N)
# Space: O(N)

