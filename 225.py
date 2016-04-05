# https://leetcode.com/problems/implement-stack-using-queues/
from Queue import Queue
class Stack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.q1 = Queue()
        self.q2 = Queue()
        

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.q2.put(x)
        while not self.q1.empty():
            self.q2.put(self.q1.get())
        self.q1, self.q2 = self.q2, self.q1
        

    def pop(self):
        """
        :rtype: nothing
        """
        return self.q1.get()
        

    def top(self):
        """
        :rtype: int
        """
        value = self.q1.get()
        t = Queue()
        t.put(value)
        while not self.q1.empty():
            t.put(self.q1.get())
        self.q1 = t
        return value

        

    def empty(self):
        """
        :rtype: bool
        """
        return self.q1.empty()
