from typing import List

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        """
        Utility function to move the first element of a list
        to its back.
        """
        def moveBack(array: List[int]):
            first: int = array[0]
            array.pop(0)
            array.append(first)
        
        """
        The idea is to generate the queueing system until
        we have skipped exactly len(students) students.
        At that point it means that a full rotation has gone
        by without anyone picking up a sandwich, meaning that
        this will never occur.
        """
        skipped: int = 0
        while len(students) > 0:
            if skipped == len(students):
                return len(students)
            first: int = students[0]
            if students[0] == sandwiches[0]:
                skipped = 0
                students.pop(0)
                sandwiches.pop(0)
            else:
                moveBack(students)
                skipped += 1
        return 0
            
        