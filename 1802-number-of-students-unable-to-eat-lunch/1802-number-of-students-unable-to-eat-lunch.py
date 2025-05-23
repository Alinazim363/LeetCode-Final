class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        failures = 0
    
        while students and sandwiches and failures < len(students):
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
                failures = 0  
            else:
                students.append(students.pop(0))
                failures += 1 
        
        return len(students)        