# Class

class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []
    
    def avg(self):
        return(sum(self.marks) / len(self.marks))
    
    @classmethod
    def friend(cls, origin, friend_name):
        # Return a new Student called 'friend_name' in the same school as self.
        return(cls(friend_name, origin.school))


class WorkingStudent(Student):
    def __init__(self, name, school, salary):
        super().__init__(name, school)
        self.salary = salary

anna = WorkingStudent('Anna', 'Oxoford', 20.00)
    
# print(anna.salary)

friend = WorkingStudent.friend(anna ,'Greg')
# print(friend.name, friend.school)

def my_method(arg1, arg2):
    return arg1 + arg2


def long_method(arg1, arg2, arg3):
    return arg1 + arg2 + arg3


def add_simp(*args):
    return sum(args)


def what_are_kwargs(*args, **kwargs):
    print(args)
    print(kwargs)


