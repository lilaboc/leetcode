# https://leetcode.com/problems/implement-queue-using-stacks/
class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.s1 = []
        self.s2 = []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        while len(self.s1) != 0:
            self.s2.append(self.s1.pop())
        self.s2.append(x)
        while len(self.s2) != 0:
            self.s1.append(self.s2.pop())
        #self.s1, self.s2 = self.s2, self.s1
        #print self.s1
        #print self.s2
        

    def pop(self):
        """
        :rtype: nothing
        """
        self.s1.pop()
        

    def peek(self):
        """
        :rtype: int
        """
        return self.s1[-1]
        

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.s1) == 0

#q = Queue()
#q.push(1)
#q.push(2)
#q.push(3)
#print q.peek()
