# https://leetcode.com/problems/my-calendar-i/

class MyCalendar:

    def __init__(self):
        self.booked = set()

    def book(self, start: int, end: int) -> bool:
        for s, e in self.booked:
            # Check overlap
            if s < end and start < e:
                return False
        self.booked.add((start, end))
        return True


# ---------------- DRIVER CODE ----------------
if __name__ == "__main__":
    cal = MyCalendar()

    print(cal.book(10, 20))  # True
    print(cal.book(15, 25))  # False (overlaps with [10,20])
    print(cal.book(20, 30))  # True (touching is allowed)
    print(cal.book(5, 10))   # True
    print(cal.book(25, 35))  # True
