class Person:
    def __init__(self,theFullName,Age,isMarried):
        self.thefullname = theFullName
        self.age = Age
        self.is_married = isMarried

    def introduce_myself(self):
         print(f'my  name is {self.thefullname}. I am {self.age } years old.I am {self.is_married}')


class Student(Person):
    def __init__(self,theFullName,Age,isMarried,Marks):
        super().__init__(theFullName,Age,isMarried)
        self.marks = Marks
    def average_mark(self):
        total_marks = sum(self.marks.values())
        return total_marks / len(self.marks)

    def introduce_myself(self):
        super().introduce_myself()
        print(f'marks are {self.marks}.average mark {self.average_mark()}')
class Teacher(Person):
    BaseSalary = 20000
    bonus = BaseSalary * 5 / 100
    def __init__(self,theFullName, Age, isMarried,Experiense):
        super().__init__(theFullName, Age, isMarried)
        self.experiense = Experiense
    def calculate_salary(self):
        while self.experiense > 3:
            self.BaseSalary += self.bonus
            self.experiense -= 1

    def introduce_myself(self):
        super().introduce_myself()
        print(f'I have been teaching for {self.experiense} years')
        print(f'my salary is {self.BaseSalary } som')

Rus_Teacher = Teacher('Pushkova Sophia Danilovna', 21,'Married',6)
Rus_Teacher.calculate_salary()
Rus_Teacher.introduce_myself()
print(Rus_Teacher)
def create_students():
   student1 = Student(' Usmanov Ali', 17, "don't married", {
        "math": 5,
        "bio": 3,
        "geo": 3,
        "phy": 4})
   student2 = Student('Saikal', 17, "don't married", {
        "math": 4,
        "bio": 4,
        "geo": 5,
        "phy": 4})
   student3 = Student("Kasymaliev Nuradil", 18,  "don't married", {
        "math": 4,
        "bio": 3,
        "geo": 5,
        "phy": 4})
   result = [student1, student2, student3]
   return result

data = create_students()
for i in data:
    i.introduce_myself()
    print(i.marks)
    i.average_mark()
    print(i.average_mark())