#print('Hola Mundo')

# Modify set2 so that set1.intersection(set2) returns {5, 77, 9, 12}
set1 = {14, 5, 9, 31, 12, 77, 67, 8}
set2 = {5, 77, 9, 12}

#print(set1.intersection(set2))

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Modify the method below to make sure only even numbers are returned.
def even_numbers():
    evens = []
    for number in numbers:
        if number % 2 == 0:
            evens.append(number)
    return evens

#print(even_numbers())


# Modify the below method so that "Quit" is returned if the choice parameter is "q".
# Don't remove the existing code
def user_menu(choice):
    if choice == "a":
        return "Add"
    if choice == 'q':
        return "Quit"

#print(user_menu('q'))

# Create a variable called student, with a dictionary.
# The dictionary must contain three keys: 'name', 'school', and 'grades'.
# The values for each must be 'Jose', 'Computing', and a tuple with the values 66, 77, and 88.
student = {
    'name' : 'Jose',
    'school' : 'Computing',
    'grades' : (66, 77, 88)
}

# Assume the argument, data, is a dictionary.
# Modify the grades variable so it accesses the 'grades' key of the data dictionary.
def average_grade(data):
    grades =   data['grades'] # Change this!
    return sum(grades) / len(grades)


# Implement the function below
# Given a list of students (a list of dictionaries), calculate the average grade received on an exam, for the entire class
# You must add all the grades of all the students together
# You must also count how many grades there are in total in the entire list
def average_grade_all_students(student_list):
    total = 0
    count = 0
    for student in student_list:
        # Implement here
        total = total + sum(student['grades'])
        count = count + len(student['grades'])

    return total / count

# Class

class LotteryPlayer:
    def __init__(self, name):
        self.name = name,
        self.numbers = (5, 9, 12, 3, 1, 21)
    
    def total(self):
        return sum(self.numbers)

player = LotteryPlayer("Rolf")

print(player.name)
print(player.numbers)
print(player.total())

p1 = LotteryPlayer("Rolf")
p1.numbers = (1, 2, 3, 6, 7, 8)
p2 = LotteryPlayer("John")

print(p1 == p2)
print(p1.numbers == p2.numbers)

## Student class

class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []
    
    def avg(self):
        return sum(self.marks) / len(self.marks)
    
    def go_to_school(self):
        print("Voy a {}".format(self.school))
    
    @classmethod
    def voy_a_la_escuela(cls):
        print('Voy a la escuela.')
    
    @staticmethod
    def voy_a_la_escuela1():
        print('Estudiante, Voy a la escuela.')


anna = Student('Anna', 'MIT')
anna.marks.append(56)
anna.marks.append(71)
anna.marks.append(99)

print(anna.marks)
print(anna.go_to_school())
print(anna.voy_a_la_escuela())
print(Student.voy_a_la_escuela1())

class Store:
    def __init__(self, name):
        # You'll need 'name' as an argument to this method.
        # Then, initialise 'self.name' to be the argument, and 'self.items' to be an empty list.
        self.name = name
        self.items = []
    
    def add_item(self, name, price):
        # Create a dictionary with keys name and price, and append that to self.items.
        item = {
            'name' : name,
            'price' : price
        }
        self.items.append(item)

    def stock_price(self):
        # Add together all item prices in self.items and return the total.
        return sum([item['price'] for item in self.items])

    @classmethod
    def franchise(cls, store):
        # Return another store, with the same name as the argument's name, plus " - franchise"
        return(cls(store.name + ' - franchise'))

    @staticmethod
    def store_details(store):
        # Return a string representing the argument
        # It should be in the format 'NAME, total stock price: TOTAL'
        return('{}, total stock price: {}'.format(store.name, store.stock_price()))


store = Store('Test')
store2 = Store('Amazon')
store2.add_item('Keyboard', 160)

Store.franchise(store) # 'Test - franchise'
Store.franchise(store2) # 'Amazon - franchise'

Store.store_details(store) # 'Test, total stock price: 0'
Store.store_details(store2) # 'Amazon, total stock price: 160'
