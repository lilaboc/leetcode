# https://leetcode.com/problems/employee-importance/description/
"""
# Employee info
class Employee(object):
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        map = {}
        for employee in employees:
            map[employee.id] = (employee.importance, employee.subordinates)
        return self.value(map, id)

    def value(self, map, id):
        return map[id][0] + sum([self.value(map, i) for i in map[id][1]])




#print Solution().getImportance([[1, 5, [2, 3]], [2, 3, []], [3, 3, []]], 1)
#print Solution().getImportance([[1,2,[2]], [2,3,[]]], 2)
