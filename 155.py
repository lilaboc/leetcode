# https://leetcode.com/problems/min-stack/

# seems using namedtuple from collections to present a node is slower than two lists

class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.arr = []
        self.mins = []
        self.min = None


    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.arr.append(x)
        self.mins.append(self.min)
        if self.min == None:
            self.min = x
        elif self.min > x:
            self.min = x


    def pop(self):
        """
        :rtype: nothing
        """
        self.arr.pop()
        self.min = self.mins.pop()



    def top(self):
        """
        :rtype: int
        """
        return self.arr[-1]


    def getMin(self):
        """
        :rtype: int
        """
        return self.min
