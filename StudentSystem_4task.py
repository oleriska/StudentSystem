class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return f'{self.name} {self.surname}'
class Student(Person):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}  

    def __str__(self):
        return f'Student: {super().__str__()}'

    def add_grade(self, subject, grade):
        self.grades[subject] = grade

    def calculate_average(self):
        if self.grades:
            return sum(self.grades.values()) / len(self.grades)
        else:
            return 0  
class Teacher(Person):
    def __init__(self, name, surname, subject_taught):
        super().__init__(name, surname)
        self.subject_taught = subject_taught

    def __str__(self):
        return f'Teacher: {super().__str__()}'
class Subject:
    def __init__(self, name, credits, bonus_scholarships):
        self.name = name
        self.credits = credits
        self.bonus_scholarships = bonus_scholarships
        self.students = []
        self.teachers = []

    def __str__(self):
        return f'Subject: {self.name}'

    def add_student(self, student):
        self.students.append(student)

    def add_teacher(self, teacher):
        self.teachers.append(teacher)

    def list_students(self):
        students_str = ', '.join(str(student) for student in self.students)
        return f'Students: {students_str}'

    def list_teachers(self):
        teachers_str = ', '.join(str(teacher) for teacher in self.teachers)
        return f' {teachers_str}'


# student objects
student1 = Student('Jonas', 'Jonaitis')
student2 = Student('John', 'Parker')
student3 = Student('Eve', 'Ella')
student4 = Student('Ann', 'Tawnie')
student5 = Student('Carol', 'Harlee')

# subject objects with credits and bonuses
math_subject = Subject('Math', credits=3, bonus_scholarships=50)
physics_subject = Subject('Physics', credits=4, bonus_scholarships=75)

# teacher objects
teacher1 = Teacher('Alice', 'Smith', 'Math')
teacher2 = Teacher('Bob', 'Johnson', 'Physics')

# Add students and teachers to subjects
math_subject.add_teacher(teacher1)
math_subject.add_student(student1)
math_subject.add_student(student2)
math_subject.add_student(student3)

physics_subject.add_teacher(teacher2)
physics_subject.add_student(student4)
physics_subject.add_student(student1)
physics_subject.add_student(student3)

# grades for students
student1.add_grade('Math', 90)
student1.add_grade('Physics', 85)
student2.add_grade('Math', 78)
student2.add_grade('Physics', 85)
student3.add_grade('Math', 95)
student3.add_grade('Physics', 88)
student4.add_grade('Math', 95)
student4.add_grade('Physics', 92)
student5.add_grade('Math', 82)
student5.add_grade('Physics', 92)

# Calculate and print student averages
print("*" * 45)
print("List of students with their average grades:")
print("*" * 45)
for student in [student1, student2, student3, student4, student5]:
    average = student.calculate_average()
    print(f'{student}: Average Grade: {average:.2f}')
print(" ")
print("List of courses:")
print(" ")
# subject details
print(math_subject)
print(f'Subject Credits: {math_subject.credits}')
print(f'Bonus Scholarships: ${math_subject.bonus_scholarships}')
print(math_subject.list_teachers())
print(math_subject.list_students())
print("-" * 43) 
print(physics_subject)
print(f'Subject Credits: {physics_subject.credits}')
print(f'Bonus Scholarships: ${physics_subject.bonus_scholarships}')
print(physics_subject.list_teachers())
print(physics_subject.list_students())
print("*" * 45)