# https://leetcode.com/problems/flatten-nested-list-iterator/
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """


class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.iterator = self.iterate(nestedList)
        self.used = False
        self.current_val = None
        

    def iterate(self, nestedList):
        for i in nestedList:
            if i.getList() != None:
                for x in self.iterate(i.getList()):
                    yield x
            else:
                yield i

    def next(self):
        """
        :rtype: int
        """
        self.used = True
        return self.current_val
        

    def hasNext(self):
        """
        :rtype: bool
        """
        try:
            if self.used or self.current_val == None:
                self.current_val = self.iterator.next()
                self.used = False
            return True
        except StopIteration, exp:
            return False

        
#i, v = NestedIterator([[1,1],2,[1,1]]), []
#while i.hasNext(): v.append(i.next())
#print v
#i, v = NestedIterator([1,[4,[6]]]), []
#while i.hasNext(): v.append(i.next())
#print v
# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
