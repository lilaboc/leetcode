# https://leetcode.com/problems/my-calendar-i/


class MyCalendar:

    def __init__(self):
        self.slots = []

    def book(self, start: int, end: int) -> bool:
        for slot in self.slots:
            if slot[0] < end and slot[1] > start:
                return False
        self.slots.append([start, end])
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)

