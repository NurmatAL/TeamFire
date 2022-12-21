class Student:
    def __init__(self, name, age, kurs):
        self.name = name
        self.age = age
        self.kurs = kurs

    def __str__(self):
        return f'<name: {self.name}, age:{self.age}, major:{self.kurs}>'

Steve = Student("Steven Schultz", 23, "English")
Johnny = Student("Jonathan Rosenberg", 24, "Biology")
Penny = Student("Penelope Meramveliotakis", 21, "Physics")
print(Steve)
print(Johnny)