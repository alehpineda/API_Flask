class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []
    
    def avg(self):
        return(sum(self.marks) / len(self.marks))
    
    @classmethod
    def friend(cls, origin, friend_name, *args, **kwargs):
        # Return a new Student called 'friend_name' in the same school as self.
        return(cls(friend_name, origin.school, *args, **kwargs))


class WorkingStudent(Student):
    def __init__(self, name, school, salary, job_title):
        super().__init__(name, school)
        self.salary = salary
        self.job_title = job_title

anna = WorkingStudent('Ana', 'Mit', 20.00, 'Software Dev')

