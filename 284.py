# https://leetcode.com/problems/peeking-iterator/


# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iter = iterator
        self.buffer = None

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if self.buffer is not None:
            return self.buffer
        else:
            self.buffer = self.iter.next()
            return self.buffer

    def next(self):
        """
        :rtype: int
        """
        if self.buffer is not None:
            r = self.buffer
            self.buffer = None
            return r
        else:
            return self.iter.next()

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.buffer is not None:
            return True
        return self.iter.hasNext()




peekingIterator = PeekingIterator(iter([1, 2, 3]));
print(peekingIterator.next())
print(peekingIterator.peek())
print(peekingIterator.next())
print(peekingIterator.next())
print(peekingIterator.hasNext())