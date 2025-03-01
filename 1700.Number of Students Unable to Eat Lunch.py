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

# 2025/02/28
# Time complexity: O(N**2)
# Space complexity: O(1)
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        all_students = False
        while not all_students and sandwiches:
            cur = sandwiches[0]
            num_students = len(students)
            idx = 0
            while idx < num_students:
                if students[idx] == cur:
                    students = students[idx + 1:] + students[: idx]
                    sandwiches.pop(0)
                    break
                else:
                    idx += 1
            all_students = (idx >= num_students)

        return len(sandwiches)