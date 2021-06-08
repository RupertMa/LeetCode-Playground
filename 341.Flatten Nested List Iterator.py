# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    from itertools import chain
    def __init__(self, nestedList: [NestedInteger]):
        self.nested = iter(nestedList)


    def next(self) -> int:
        cur = next(self.nested)
        return cur.getInteger()

    def hasNext(self) -> bool:
        cur = next(self.nested, False)
        if cur!=False and cur.isInteger():
            self.nested = chain([cur], self.nested)
            return True
        elif cur!=False and (not cur.isInteger()):
            self.nested = chain(cur.getList(), self.nested)
            return self.hasNext()
        else:
            return cur
# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
