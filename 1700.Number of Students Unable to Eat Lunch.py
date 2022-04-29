from typing import List

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        length = len(students)
        while length:
            cur_student = students.pop(0)
            cur_sandwiches = sandwiches[0]
            if cur_student == cur_sandwiches:
                _ = sandwiches.pop(0)
                length = len(students)
            else:
                students.append(cur_student)
                length -= 1
        return len(students)

        # Time complexity: O(N**2)
        # Space complexity: O(1)
