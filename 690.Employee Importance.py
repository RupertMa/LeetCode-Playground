"""
# Employee info
class Employee:
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
class Solution:
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        unionFind = {}
        ans = 0
        for employee in employees:
            unionFind[employee.id] = (employee.subordinates, employee.importance)
        stack = unionFind[id][0]
        while stack:
            sub = stack.pop()
            subs, importance = unionFind[sub] 
            stack.extend(subs)
            unionFind[id] = (unionFind[id][0], unionFind[id][1] + importance)
        return unionFind[id][1]