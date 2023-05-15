# https://leetcode.com/problems/frequency-tracker/

from collections import Counter

class FrequencyTracker:

    def __init__(self):
        self.c = Counter()
        self.s = None

    def add(self, number: int) -> None:
        self.s = None
        self.c[number] += 1

    def deleteOne(self, number: int) -> None:
        if number in self.c:
            self.s = None
            self.c[number] -= 1
            if self.c[number] == 0:
                self.c.pop(number)


    def hasFrequency(self, frequency: int) -> bool:
        if not self.s:
            self.s = set(self.c.values())
        return frequency in self.s

# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)