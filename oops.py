class Student:
    # constructor method
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    # method
    def average(self):
        return sum(self.grades) / len(self.grades)


stud = Student("Pratik", (90, 80, 87, 85))
print(stud.name)
print(stud.average())

stud2 = Student("Pawar", (90, 100, 87, 85))
print(stud2.name)
print(stud2.average())
